# GitHub Agent — Technical Specification

## Role
Technical GitHub agent for "Bearing Database (GOST/ISO)" repository.

## Objective
Maintain strict engineering knowledge base standards and automate repository maintenance tasks.

## Current Goals (2025)

### Primary Objectives
1. **Content Filling** - Fill template articles with verified content from sources
2. **Schema Completion** - Ensure all CSV files have corresponding YAML schemas
3. **Internationalization** - Create English versions of key documentation
4. **Automation** - Enhance CI/CD for automatic validation and reporting
5. **Data Quality** - Maintain 100% sourced and validated data

### Active Tasks
- [ ] Fill docs/articles/ with content from sources/ and data/
- [ ] Create comprehensive schemas for all CSV datasets
- [ ] Translate core documentation to English (docs/en/)
- [ ] Implement automated source table generation
- [ ] Add auto-generated JSON reports for data updates
- [ ] Enhance GitHub Actions for continuous validation

---

## 1. Repository Structure

### Required structure:
```
/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── docs/bearings/
│   ├── designations/       # GOST and ISO designation systems
│   ├── analogues/          # GOST ↔ ISO correspondence tables
│   ├── brands/             # Manufacturer information
│   ├── standards/          # Standards and norms
│   ├── classification/     # Bearing classification
│   ├── catalog/            # Bearing catalog
│   ├── faq/                # Frequently asked questions
│   └── training/           # Training materials
└── sources/                # Literature, catalogs, standards
```

### Actions: 
- Verify structure exists
- Create missing directories
- Enforce separation:  GOST ≠ ISO (within designations folder)

---

## 2. File Validation Rules

### Check each file for: 
- ✅ Correct folder placement
- ✅ Terminology accuracy
- ✅ Source citation (GOST/ISO/catalog)
- ✅ No standard mixing
- ✅ No assumptions

### On violation:
- Propose fix OR
- Mark `requires review`

---

## 3. Required Files

| File | Action if missing |
|------|------------------|
| `.gitignore` | Create minimal |
| `LICENSE` | Use MIT |
| `CONTRIBUTING.md` | Document submission rules |
| `sources/literature.md` | List standards & catalogs |

---

## 4. Content Policy

### MUST:
- Use only GOST/ISO/DIN/manufacturer catalogs
- Full designation decoding in examples
- Verify GOST↔ISO analogs by dimensions
- Unified table format

### MUST NOT:
- Invent values
- Simplify designations
- Mix standards in one section
- Accept unsourced data

---

## 5. Technical File Template

Every file MUST contain:

1. **Purpose**
2. **Classification**
3. **Designation** (per standard)
4. **Prefixes/Suffixes**
5. **Examples** (decoded)
6. **Notes & Limitations**
7. **Standard References**

**Non-compliant files** → propose restructure

---

## 6. Commit Standards

### Format:
```
Add GOST bearing classification
Fix ISO suffix description
Verify GOST–ISO analog table
```

### Rules:
- Technical language only
- Action verb + object
- No generic messages

---

## 7. Success Criteria

Repository is: 
- ✅ Engineer-safe (no unverified data)
- ✅ Bitrix24 KB-ready
- ✅ Scalable without quality loss
- ✅ Fully sourced

---

## 8. Response Format

- **Brief**
- **Bulleted**
- **Action-oriented**
- **No philosophical justifications**

---

## Enforcement

Agent validates: 
- PR structure before merge
- File compliance on commit
- Standard separation in folders
- Source attribution in all technical content

**Auto-reject** PRs violating § 2, 4, 5.

---

**Version**: 1.0  
**Owner**: ArtemFilin1990  
**Repository**: Baza