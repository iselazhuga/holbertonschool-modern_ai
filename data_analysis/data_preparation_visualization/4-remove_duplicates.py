#!/usr/bin/env python3
"""Remove duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Return df without its duplicate rows, keeping the first of each."""
    return df.drop_duplicates()
