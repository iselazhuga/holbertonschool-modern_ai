#!/usr/bin/env python3
"""Welch's t-tests between numeric features and Churn."""
from scipy import stats


def ttest_numeric(df):
    """Return {feature: p_value} of Welch's t-test for each numeric column.

    Compares the mean of the column for Churn 'Yes' and Churn 'No'
    without assuming equal variances.
    """
    churned = df['Churn'] == 'Yes'
    results = {}
    for col in df.select_dtypes(include='number').columns:
        _, p_value = stats.ttest_ind(df.loc[churned, col],
                                     df.loc[~churned, col],
                                     equal_var=False)
        results[col] = p_value
    return results
