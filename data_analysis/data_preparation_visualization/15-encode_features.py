#!/usr/bin/env python3
"""Encode the features of the churn dataset for modeling."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode df and return it with the fitted encoders.

    Churn uses a LabelEncoder, the Yes/No columns an OrdinalEncoder,
    Contract and PaymentMethod one-hot encoding (first level dropped) and
    TenureGroup an OrdinalEncoder in alphabetical order.
    Returns (encoded df, churn encoder, binary encoder, tenure encoder).
    """
    df = df.copy()

    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                   'SeniorCitizen']
    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    for col in binary_cols:
        df[col] = binary_oe.fit_transform(df[[col]]).astype(int).ravel()

    tenure_oe = preprocessing.OrdinalEncoder()
    tenure = df[['TenureGroup']].astype(str)
    df['TenureGroup'] = tenure_oe.fit_transform(tenure).astype(int).ravel()

    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True, dtype=int)
    return df, churn_le, binary_oe, tenure_oe
