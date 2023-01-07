#!/usr/bin/env python3
import os
import sys
import pandas as pd

DEST = os.environ['DEST']


def read_csv(filename: str):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['month'] = df['date'].dt.month
    return df


if __name__ == '__main__':
    dfs = [read_csv(filename) for filename in sys.argv[1:]]
    df = pd.concat(dfs)
    df = df.drop_duplicates(subset=['url', 'month'])

    desc = df.groupby(['month', 'district'])['rental_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9])

    print(desc)

    desc.to_csv(DEST)
