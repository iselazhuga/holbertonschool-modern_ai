#!/usr/bin/env python3
"""Standardize the MonthlyCharges and TotalCharges columns."""
from sklearn import preprocessing


def scale_numeric(df):
    """Return df with MonthlyCharges and TotalCharges standardized.

    Each column is rescaled to mean 0 and standard deviation 1.
    """
    df = df.copy()
    columns = ['MonthlyCharges', 'TotalCharges']
    scaler = preprocessing.StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
