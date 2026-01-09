#!/usr/bin/env python3
"""
Scraper for table data that crawls all pagination links and exports the
resulting rows into a JSON file under sources/.

The script is intentionally dependency-free (stdlib only) to simplify execution
in restricted environments. Network timeouts, page limits and delays are
configurable via CLI flags or environment variables:

  HTTP_TIMEOUT_SECONDS   - request timeout (default: 10)
  REQUEST_DELAY_SECONDS  - delay between pages in seconds (default: 0.2)
  TABLE_MAX_PAGES        - hard cap for visited pages (default: 250)
  TABLE_SCRAPER_USER_AGENT - optional override for the HTTP User-Agent
  TABLE_MAX_RETRIES      - maximum retry attempts for failed requests (default: 3)
  TABLE_RETRY_DELAY      - delay between retry attempts in seconds (default: 2.0)

Example:
    python sources/table_scraper.py \\
        --output sources/table_data.json \\
        --max-retries 5 \\
        --retry-delay 3.0

If network access is blocked, the script will log a warning and exit without
creating or altering the output file.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from collections import deque
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen

DEFAULT_TIMEOUT_SECONDS = int(os.getenv("HTTP_TIMEOUT_SECONDS", "10"))
DEFAULT_DELAY_SECONDS = float(os.getenv("REQUEST_DELAY_SECONDS", "0.2"))
DEFAULT_MAX_PAGES = int(os.getenv("TABLE_MAX_PAGES", "250"))
DEFAULT_USER_AGENT = os.getenv("TABLE_SCRAPER_USER_AGENT", "TableScraper/1.0")
DEFAULT_MAX_RETRIES = int(os.getenv("TABLE_MAX_RETRIES", "3"))
DEFAULT_RETRY_DELAY = float(os.getenv("TABLE_RETRY_DELAY", "2.0"))


def configure_logging(verbosity: int) -> None:
    """Configure structured logging with level based on the verbosity flag."""
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )


def clean_text(raw: str) -> str:
    """Collapse whitespace and strip surrounding spaces for table cell content."""
    return re.sub(r"\s+", " ", raw).strip()


@dataclass
class TableCell:
    text: str
    is_header: bool


class TableHTMLParser(HTMLParser):
    """Minimal HTML table extractor without external dependencies."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[TableCell]]] = []
        self._current_table: list[list[TableCell]] | None = None
        self._current_row: list[TableCell] | None = None
        self._current_cell: list[str] = []
        self._current_is_header = False
        self._table_depth = 0

    def handle_starttag(self, tag: str, attrs: Sequence[tuple[str, str | None]]) -> None:
        if tag == "table":
            self._table_depth += 1
            if self._table_depth == 1:
                self._current_table = []
        if self._table_depth == 0:
            return
        if tag == "tr":
            self._current_row = []
        elif tag in {"td", "th"}:
            self._current_cell = []
            self._current_is_header = tag == "th"

    def handle_data(self, data: str) -> None:
        if self._table_depth and self._current_cell is not None:
            self._current_cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._table_depth == 0:
            return
        if tag in {"td", "th"} and self._current_row is not None:
            text = clean_text("".join(self._current_cell))
            if text:
                self._current_row.append(TableCell(text=text, is_header=self._current_is_header))
            self._current_cell = []
        elif tag == "tr":
            if self._current_table is not None and self._current_row:
                self._current_table.append(self._current_row)
            self._current_row = None
        elif tag == "table":
            if self._table_depth == 1 and self._current_table:
                self.tables.append(self._current_table)
            self._current_table = None
            self._table_depth = max(0, self._table_depth - 1)


class AnchorParser(HTMLParser):
    """Collect anchor hrefs for pagination discovery."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: Sequence[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.add(href)


def normalize_url(url: str) -> str:
    """Normalize URL for deduplication by sorting query params and dropping fragments."""
    parsed = urlparse(url)
    sorted_query = urlencode(sorted(parse_qsl(parsed.query)))
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", sorted_query, ""))


def is_same_resource(target_url: str, base_url: str) -> bool:
    """Restrict crawling to the same path as the base resource."""
    base_path = urlparse(base_url).path
    return urlparse(target_url).path == base_path


def extract_tables(html: str) -> list[list[list[TableCell]]]:
    parser = TableHTMLParser()
    parser.feed(html)
    return parser.tables


def extract_links(html: str, base_url: str) -> set[str]:
    parser = AnchorParser()
    parser.feed(html)
    links: set[str] = set()
    for raw_href in parser.links:
        absolute = urljoin(base_url, raw_href)
        if is_same_resource(absolute, base_url):
            links.add(normalize_url(absolute))
    return links


def select_primary_table(tables: list[list[list[TableCell]]]) -> list[list[TableCell]] | None:
    if not tables:
        return None
    return max(tables, key=len)


def derive_headers(table: list[list[TableCell]]) -> list[str]:
    for row in table:
        if any(cell.is_header for cell in row):
            return [_normalize_header(cell.text, idx) for idx, cell in enumerate(row, start=1)]
    reference_width = len(table[0]) if table else 0
    return [_normalize_header(f"column_{idx}", idx) for idx in range(1, reference_width + 1)]


def _normalize_header(text: str, position: int) -> str:
    normalized = re.sub(r"[^0-9A-Za-zА-Яа-я_]+", "_", text.strip())
    normalized = re.sub(r"_+", "_", normalized).strip("_").lower()
    return normalized or f"column_{position}"


def table_to_records(table: list[list[TableCell]]) -> list[dict[str, str]]:
    if not table:
        return []
    headers = derive_headers(table)
    records: list[dict[str, str]] = []
    for row in table:
        if all(cell.is_header for cell in row):
            continue
        record: dict[str, str] = {}
        for idx, header in enumerate(headers):
            value = row[idx].text if idx < len(row) else ""
            record[header] = value
        records.append(record)
    return records


def fetch_html(
    url: str, timeout: int, max_retries: int = DEFAULT_MAX_RETRIES, retry_delay: float = DEFAULT_RETRY_DELAY
) -> str:
    """
    Fetch HTML with retry logic for transient network errors.

    Args:
        url: URL to fetch
        timeout: Request timeout in seconds
        max_retries: Maximum number of retry attempts (default: 3)
        retry_delay: Delay between retries in seconds (default: 2.0)

    Returns:
        str: HTML content decoded as UTF-8

    Raises:
        HTTPError: If HTTP request fails after all retries
        URLError: If network connection fails after all retries
        ValueError: If max_retries is less than 0
    """
    if max_retries < 0:
        raise ValueError("max_retries must be at least 0")

    request = Request(url, headers={"User-Agent": DEFAULT_USER_AGENT})
    last_error: Exception | None = None

    for attempt in range(max_retries):
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read().decode(response.headers.get_content_charset("utf-8"), errors="replace")
        except (HTTPError, URLError) as error:
            last_error = error
            if attempt < max_retries - 1:
                logging.warning(
                    "Attempt %d/%d failed for %s: %s. Retrying in %.1fs...",
                    attempt + 1,
                    max_retries,
                    url,
                    error,
                    retry_delay,
                )
                time.sleep(retry_delay)
            else:
                logging.error("All %d attempts failed for %s: %s", max_retries, url, error)

    # This should never happen since we always set last_error in the loop, but for type safety
    if last_error is None:
        raise RuntimeError(f"Unexpected error: fetch failed but no error was captured for {url}")

    raise last_error


def crawl_all_pages(
    base_url: str,
    timeout_seconds: int,
    delay_seconds: float,
    max_pages: int,
    max_retries: int = DEFAULT_MAX_RETRIES,
    retry_delay: float = DEFAULT_RETRY_DELAY,
) -> list[dict[str, str]]:
    visited: set[str] = set()
    queue: deque[str] = deque([normalize_url(base_url)])
    aggregated_rows: list[dict[str, str]] = []
    failed_urls: list[str] = []

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        logging.info("Fetching %s (page %d/%d)", url, len(visited) + 1, max_pages)
        try:
            html = fetch_html(url, timeout_seconds, max_retries, retry_delay)
        except (HTTPError, URLError) as error:
            logging.warning("Failed to fetch %s after %d retries: %s", url, max_retries, error)
            failed_urls.append(url)
            # Continue to next URL instead of breaking
            continue
        visited.add(url)
        tables = extract_tables(html)
        primary_table = select_primary_table(tables)
        if primary_table:
            page_records = table_to_records(primary_table)
            logging.info("Extracted %d rows from %s", len(page_records), url)
            aggregated_rows.extend(page_records)
        else:
            logging.warning("No tables found on %s", url)

        for link in extract_links(html, url):
            if link not in visited and link not in queue and len(visited) + len(queue) < max_pages:
                queue.append(link)

        time.sleep(delay_seconds)

    if failed_urls:
        if len(failed_urls) <= 5:
            logging.warning("Failed to fetch %d URLs: %s", len(failed_urls), failed_urls)
        else:
            logging.warning("Failed to fetch %d URLs (showing first 5): %s", len(failed_urls), failed_urls[:5])

    return aggregated_rows


def dump_results(rows: list[dict[str, str]], output_path: str, source_url: str) -> None:
    payload = {
        "source": source_url,
        "retrieved_at": datetime.now(UTC).isoformat(),
        "row_count": len(rows),
        "rows": rows,
    }
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl table data and export into JSON.")
    parser.add_argument(
        "--url",
        default="https://example.com/table.php",
        help="Base URL to crawl (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default="sources/table_data.json",
        help="Output JSON path (default: %(default)s)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help="Request timeout in seconds (default: %(default)s)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_SECONDS,
        help="Delay between requests in seconds (default: %(default)s)",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help="Maximum number of pages to crawl (default: %(default)s)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase log verbosity (can be repeated)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        help="Maximum number of retry attempts for failed requests (default: %(default)s)",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=DEFAULT_RETRY_DELAY,
        help="Delay between retry attempts in seconds (default: %(default)s)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    configure_logging(args.verbose)
    logging.info(
        "Starting crawl: url=%s, max_pages=%d, timeout=%ds, delay=%.2fs, max_retries=%d",
        args.url,
        args.max_pages,
        args.timeout,
        args.delay,
        args.max_retries,
    )
    rows = crawl_all_pages(
        base_url=args.url,
        timeout_seconds=args.timeout,
        delay_seconds=args.delay,
        max_pages=args.max_pages,
        max_retries=args.max_retries,
        retry_delay=args.retry_delay,
    )
    if not rows:
        logging.warning("No rows extracted; output file will not be created.")
        return 1
    dump_results(rows, args.output, args.url)
    logging.info("Saved %d rows into %s", len(rows), args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
