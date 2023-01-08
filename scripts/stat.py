#!/usr/bin/env python3
import os
import sys
import pandas as pd

DEST_DIR = os.environ['DEST_DIR']


def read_csv(filename: str):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['month'] = df['date'].dt.month
    return df


if __name__ == '__main__':
    dfs = [read_csv(filename) for filename in sys.argv[1:]]
    df = pd.concat(dfs)
    df = df.drop_duplicates(subset=['url', 'month'])

    df['rental_per_area_by_month'] = df['rental_by_month'] / df['area']

    print('# Rental monthly by district')

    df.groupby(['month', 'district'])['rental_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9]) \
        .to_csv(os.path.join(DEST_DIR, 'rental-monthly-by-district.csv'))

    print('# Rental per area monthly by district')

    df.groupby(['month', 'district'])['rental_per_area_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9]) \
        .to_csv(os.path.join(DEST_DIR, 'rental-per-area-monthly-by-district.csv'))

    print('# Uniq url data')

    uniq_url_df = df.groupby(['url'])[['rental_by_month', 'rental_per_area_by_month']].median()
    uniq_url_df = pd.merge(uniq_url_df,
                           df[['url', 'district', 'subdistrict']].drop_duplicates(subset=['url']),
                           on='url', how='left')

    uniq_url_df.groupby('district')['rental_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9]) \
        .to_csv(os.path.join(DEST_DIR, 'rental-all-by-district.csv'))

    uniq_url_df.groupby(['district', 'subdistrict'])['rental_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9]) \
        .to_csv(os.path.join(DEST_DIR, 'rental-all-by-subdistrict.csv'))

    uniq_url_df.groupby('district')['rental_per_area_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9]) \
        .to_csv(os.path.join(DEST_DIR, 'rental-per-area-all-by-district.csv'))

    uniq_url_df.groupby(['district', 'subdistrict'])['rental_per_area_by_month'] \
        .describe(percentiles=[0.5, 0.8, 0.9]) \
        .to_csv(os.path.join(DEST_DIR, 'rental-per-area-all-by-subdistrict.csv'))

    print('Done')
