#!/usr/bin/env python3
"""Create the NumServices and TenureGroup features."""
import pandas as pd


def create_features(df):
    """Return df with NumServices and TenureGroup instead of their sources.

    NumServices counts the services with 'Yes' (any InternetService other
    than 'No' counts as one). TenureGroup bins tenure into 0-12, 13-24,
    25-48, 49-60 and 60+, upper bounds included.
    """
    df = df.copy()
    services = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV',
                'StreamingMovies']
    df['NumServices'] = ((df[services] == 'Yes').sum(axis=1)
                         + (df['InternetService'] != 'No').astype(int))
    df['TenureGroup'] = pd.cut(df['tenure'],
                               bins=[0, 12, 24, 48, 60, float('inf')],
                               labels=['0-12', '13-24', '25-48', '49-60',
                                       '60+'])
    return df.drop(columns=services + ['InternetService', 'tenure'])
