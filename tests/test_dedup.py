from scripts.update_repo import _dedupe


def test_deduplication_keeps_first_match() -> None:
    rows = [
        {"gost": "6205", "iso": "6305", "brand": "", "notes": ""},
        {"gost": "6205", "iso": "6305", "brand": "SKF", "notes": "duplicate"},
        {"gost": "7205", "iso": "30205", "brand": "", "notes": ""},
    ]

    deduped, removed = _dedupe(rows, ["gost", "iso"])

    assert removed == 1
    assert deduped[0]["iso"] == "6305"
    assert len(deduped) == 2
