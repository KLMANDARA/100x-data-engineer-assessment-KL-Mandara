#!/usr/bin/env python3
"""
validate_results.py
Simple validator to run SQL queries and assert expected outputs.
Usage:
  python scripts/validate_results.py --db sqlite:///assessment.db --query sql/task1.sql
"""
import argparse
from sqlalchemy import create_engine, text
import pandas as pd

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--db', default='sqlite:///assessment.db')
    p.add_argument('--query', required=True)
    return p.parse_args()

def main():
    args = parse_args()
    engine = create_engine(args.db)
    with open(args.query, 'r') as f:
        q = f.read()
    df = pd.read_sql_query(text(q), engine)
    print(df.head().to_csv(index=False))
    # Add assertions or checks as required

if __name__ == '__main__':
    main()
