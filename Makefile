.PHONY: help install install-dev lint format test dedup validate ci docker-build docker-up docker-down clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	python -m pip install --upgrade pip
	pip install -r requirements.txt

install-dev: install ## Install development dependencies
	pip install -r requirements-dev.txt
	pre-commit install

lint: ## Run code linters
	@echo "Running ruff..."
	ruff check scripts/ sources/ tests/
	@echo "Running mypy..."
	mypy scripts/ sources/ tests/ --ignore-missing-imports
	@echo "Checking code style with black..."
	black --check scripts/ sources/ tests/

format: ## Format code with black and ruff
	@echo "Formatting with black..."
	black scripts/ sources/ tests/
	@echo "Fixing with ruff..."
	ruff check --fix scripts/ sources/ tests/

test: ## Run tests with pytest
	pytest -v

test-cov: ## Run tests with coverage
	pytest --cov=scripts --cov=sources --cov-report=html --cov-report=term

dedup: ## Run deduplication on nomenclature.csv
	python scripts/deduplicate_nomenclature.py

validate: ## Validate CSV files
	python scripts/validate/run_validations.py

ci: lint test validate ## Run full CI pipeline locally
	@echo "✅ All CI checks passed!"

docker-build: ## Build Docker image
	docker build -t baza:latest .

docker-up: ## Start Docker containers
	docker-compose up -d

docker-down: ## Stop Docker containers
	docker-compose down

clean: ## Clean build artifacts and cache
	find . -type d -name "__pycache__" -print0 | xargs -0 rm -rf 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -print0 | xargs -0 rm -rf 2>/dev/null || true
	find . -type d -name ".ruff_cache" -print0 | xargs -0 rm -rf 2>/dev/null || true
	find . -type d -name ".mypy_cache" -print0 | xargs -0 rm -rf 2>/dev/null || true
	find . -type d -name "*.egg-info" -print0 | xargs -0 rm -rf 2>/dev/null || true
	rm -rf coverage_html/ htmlcov/ .coverage
	@echo "✅ Cleaned build artifacts and cache"
