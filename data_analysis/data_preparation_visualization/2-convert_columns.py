#!/usr/bin/env python3
"""Fix the types of the TotalCharges and SeniorCitizen columns."""
import pandas as pd


def convert_columns(df):
    """Return df with TotalCharges numeric and SeniorCitizen as No/Yes.

    Values of TotalCharges that are not numbers become NaN.
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
