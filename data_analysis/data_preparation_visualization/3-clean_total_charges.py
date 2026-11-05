#!/usr/bin/env python3
"""Handle the missing values of TotalCharges."""


def clean_total_charges(df, method='drop'):
    """Return a copy of df with the missing TotalCharges handled.

    method 'drop' removes those rows, 'median' fills them with the column
    median and 'impute' fills them with MonthlyCharges * tenure.
    """
    df = df.copy()
    missing = df['TotalCharges'].isna()
    if method == 'drop':
        df = df[~missing]
    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['TotalCharges'].median())
    elif method == 'impute':
        df.loc[missing, 'TotalCharges'] = (
            df.loc[missing, 'MonthlyCharges'] * df.loc[missing, 'tenure'])
    return df
