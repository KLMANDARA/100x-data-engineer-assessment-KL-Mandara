# 100x Data Engineer Assessment — K L Mandara

## Overview
This repo contains my solutions for the 100x Data Engineer at-home assessment.  
Languages / tools used: Python 3.10, SQLite/Postgres (SQL), pandas, argparse, SQL scripts, Git.

## Repo structure
```
README.md
sql/
  setup.sql
  task1.sql
  task2.sql
scripts/
  etl.py
  validate_results.py
notebooks/         (optional)
data/              (small sample data)
results/           (outputs/screenshots)
requirements.txt
```

## How to run (local, minimal)
1. Clone repo:
   ```bash
   git clone https://github.com/<your-username>/100x-data-engineer-assessment-KL-Mandara.git
   cd 100x-data-engineer-assessment-KL-Mandara
   ```
2. Create virtual env & install:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. Initialize DB (SQLite example):
   ```bash
   sqlite3 assessment.db < sql/setup.sql
   ```
4. Run SQL solutions (example for task 1):
   ```bash
   sqlite3 assessment.db < sql/task1.sql > results/task1_output.csv
   ```
5. Run ETL script:
   ```bash
   python scripts/etl.py --input data/sample.csv --output results/out.json
   ```

## Files / folders
- `sql/` — SQL files; each solution has the question header as a comment.
- `scripts/` — Python scripts for ETL, validations, and helper utilities.
- `data/` — small sample data to reproduce results quickly.
- `results/` — files and screenshots of outputs.
- `requirements.txt` — required Python packages.

## Assumptions & Notes
- Default DB used: SQLite for quick testing; scripts support Postgres (see README section 'DB Config').
- Any large datasets are not included; `data/` contains small samples and schema.
- All steps were tested on Python 3.10.

## Contact
K L Mandara — klmandara5@gmail.com —
 +91 9380484533  

