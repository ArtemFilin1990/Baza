# Quick Start Example

## 1. Create test bearing data

```bash
mkdir -p inbox
cat > inbox/bearings.csv << 'EOF'
Артикул,Бренд,d,D,H
6200,SKF,10,30,9
6201,FAG,12,32,10
6202,NSK,15,35,11
EOF
```

## 2. Process the file (once mode)

```bash
python -m src.cli once
```

или

```bash
./bin/run once
```

## 3. Check results

```bash
# View catalog
cat out/catalog_target.csv

# View report
cat out/run_report.ndjson

# Check processed file
ls -la processed/
```

Expected output:

```
out/catalog_target.csv:
Наименование,Артикул,Аналог,Бренд,D,d,H,m
,6200,,SKF,30.0,10.0,9.0,
,6201,,FAG,32.0,12.0,10.0,
,6202,,NSK,35.0,15.0,11.0,

processed/:
20260123_123456__bearings__3__5916956a.csv
```

## 4. Test idempotency

Copy the same file again:

```bash
cp processed/20260123_*.csv inbox/bearings2.csv
python -m src.cli once
```

The file will be skipped (duplicate content detected) and no new records will be added to the catalog.

## 5. Watch mode (continuous monitoring)

```bash
python -m src.cli watch
```

This will continuously monitor the `inbox/` directory for new files and process them automatically. Press `Ctrl+C` to stop.
