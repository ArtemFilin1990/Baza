# Database: GOST and ISO Bearings

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](docs/bearings/selection_guide.md)
![Status](https://img.shields.io/badge/status-active-success.svg)

> Comprehensive reference system for rolling bearings according to GOST and ISO standards

## Project Description

A reference database for rolling bearings that comply with GOST and ISO standards. The project includes technical documentation, specifications, classification, designations, analogs, and selection recommendations, as well as training materials.

### ✨ Key Features

- 🔍 **Analog Search** - quick selection of GOST ↔ ISO equivalents
- 📊 **Technical Specifications** - complete bearing specifications
- 🏭 **Manufacturer Database** - information about brands and suppliers
- 📖 **Training Materials** - guides for specialists
- 🔧 **Selection Guides** - step-by-step selection instructions
- 💾 **Structured Data** - CSV files with dimensions, tolerances, analogs
- 🛠️ **Processing Tools** - Python scripts for validation and data normalization

## 📑 Quick Start

### Main Documents
- [📖 Bearing Selection Guide](docs/bearings/selection_guide.md) - **Main selection document**
- [👨‍💼 Manager's Guide](docs/bearings/training/managers_guide.md) - **Training material**

### Data and Tools
- [Structured Data](data/) - CSV files:
  - **GOST**: bearings.csv, dimensions.csv, series.csv, tolerances.csv
  - **ISO**: bearings.csv, dimensions.csv, prefixes.csv, suffixes.csv
  - **Analogs**: gost_iso.csv, units.csv, housings.csv
  - **Brands**: brands.csv with manufacturer information
- [Python Scripts](scripts/) - validation, normalization, data extraction, testing
- [Data Navigation](INDEX.md) - detailed index of all data

## Repository Structure

```
Baza/
├── data/           # 📊 Data in CSV format (GOST, ISO, analogs, brands)
├── docs/           # 📚 Documentation and articles
├── schemas/        # 📋 Data schemas (YAML)
├── scripts/        # 🛠️ Processing and validation scripts
├── sources/        # 🔧 Source materials (PDFs, catalogs, standards)
└── tests/          # ✅ Tests
```

## Installation and Usage

### Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/ArtemFilin1990/Baza.git
   cd Baza
   ```

2. Install dependencies for Python scripts:
   ```bash
   pip install -r requirements.txt
   ```

3. Start with the main guide:
   - [📖 Bearing Selection Guide](docs/bearings/selection_guide.md)
   - [👨‍💼 Manager's Guide](docs/bearings/training/managers_guide.md)

### Working with Data

**Data normalization:**
```bash
python scripts/update_repo.py
```

**Data validation:**
```bash
python scripts/validate/run_validations.py
```

**Running tests:**
```bash
pytest tests/
```

## Contributing

We welcome contributions to the project! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### How to Contribute

1. Fork the repository
2. Create a branch for your feature
3. Make changes and validate them
4. Commit and open a Pull Request

### Guidelines
- Use clear commit messages
- Document added code
- Follow existing coding style
- Add tests for new functionality
- Validate CSV data before committing
- Cite sources for all technical data (GOST, ISO, catalogs)

## Related Resources

- [GOST 520-2002](http://docs.cntd.ru/) - Rolling bearings. General specifications
- [GOST 3478-2012](http://docs.cntd.ru/) - Basic standards of interchangeability
- [GOST 24810-2013](http://docs.cntd.ru/) - Rolling bearings. Internal design

## Technical Support

For questions about using the database:
- GitHub Issues: [create issue](../../issues)
- Email: support@example.com

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Note**: This database is for reference purposes. For critical applications, always verify with current GOST standards and manufacturer technical documentation.

## Version and Updates

**Current version:** 1.0.1  
**Last update:** December 2025

---

© 2025 ArtemFilin1990. All rights reserved.
