#!/usr/bin/env python3
"""
etl.py
Simple ETL skeleton: read CSV, transform, write JSON/DB.
Usage:
  python scripts/etl.py --input data/sample.csv --output results/out.json
"""
import argparse
import pandas as pd
from sqlalchemy import create_engine

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--db', default='', help='Optional DB connection string (sqlite:///assessment.db)')
    return p.parse_args()

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Example transform: lowercase column names, fillna, type casts
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.fillna({'value': 0})
    # Add more domain-specific transforms here
    return df

def main():
    args = parse_args()
    df = pd.read_csv(args.input)
    df_t = transform(df)
    df_t.to_json(args.output, orient='records', lines=True)
    if args.db:
        engine = create_engine(args.db)
        df_t.to_sql('staging_table', engine, if_exists='replace', index=False)
    print("ETL complete. Output written to", args.output)

if __name__ == '__main__':
    main()
