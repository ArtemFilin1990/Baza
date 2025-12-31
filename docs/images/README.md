# Images and Diagrams

This directory contains images, diagrams, and illustrations used in the documentation.

## Structure

```
images/
├── diagrams/         # Technical diagrams and schematics
├── logos/           # Brand and manufacturer logos
├── charts/          # Charts and graphs
└── photos/          # Product photos and examples
```

## Guidelines

### Adding Images

1. **File naming**: Use descriptive names in English
   - Good: `bearing_cross_section.png`
   - Bad: `img1.png`

2. **Formats**:
   - PNG for diagrams and screenshots
   - SVG for vector graphics
   - JPEG for photos (optimized, <500KB)

3. **Size**: Optimize images before committing
   - Max width: 1200px for diagrams
   - Max width: 800px for photos
   - Use appropriate compression

4. **Attribution**: If using external images, add source in commit message

### Using Images in Documentation

Reference images using relative paths:

```markdown
![Bearing cross-section diagram](../images/diagrams/bearing_cross_section.png)
```

For articles in subdirectories:

```markdown
![SKF Logo](../../images/logos/skf_logo.png)
```

## Image Categories

### Diagrams
- Bearing construction diagrams
- Installation schemes
- Dimension drawings
- Load distribution diagrams

### Logos
- Manufacturer logos
- Brand logos
- Standard organization logos (ISO, GOST, etc.)

### Charts
- Performance charts
- Load capacity graphs
- Temperature range charts
- Comparison tables (visual)

### Photos
- Product examples
- Installation examples
- Damage examples
- Quality inspection examples

## Copyright and Licensing

- Only use images you have rights to use
- Prefer open-source or public domain images
- When using manufacturer images, ensure compliance with their terms
- Add attribution where required

## TODO

- [ ] Add bearing type diagrams (ball, roller, needle, etc.)
- [ ] Add installation procedure diagrams
- [ ] Add dimension drawing templates
- [ ] Add manufacturer logos (with permission)
- [ ] Add comparison charts for bearing types
- [ ] Add damage pattern photos for diagnostics
