#!/usr/bin/env python3
"""Remove the customerID column, which has no predictive value."""


def drop_customerID(df):
    """Return df without the customerID column."""
    return df.drop(columns=['customerID'])
