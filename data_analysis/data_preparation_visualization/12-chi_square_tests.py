#!/usr/bin/env python3
"""Chi-square tests between categorical features and Churn."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Return {feature: p_value} of the chi-square test against Churn.

    Every column of dtype object except Churn itself is tested.
    """
    results = {}
    for col in df.select_dtypes(include='object').columns:
        if col == 'Churn':
            continue
        table = pd.crosstab(df[col], df['Churn'])
        _, p_value, _, _ = stats.chi2_contingency(table)
        results[col] = float(p_value)
    return results
