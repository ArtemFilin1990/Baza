# Example Bearing Data Files

Sample data files for the automated bearings catalog processing pipeline.

## Files

- **sample_data.csv** - CSV with Russian column names
- **sample_data.json** - JSON with mixed column names

## Usage

```bash
# Start watcher
python -m src.cli watch

# Copy sample to inbox (in another terminal)
cp examples/sample_data.csv inbox/
```
