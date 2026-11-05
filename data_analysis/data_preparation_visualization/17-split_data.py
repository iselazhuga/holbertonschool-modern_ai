#!/usr/bin/env python3
"""Split the dataset into stratified train and test sets."""
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """Return X_train, X_test, y_train, y_test split from df.

    The split is stratified on target so both sets keep the same share
    of each class.
    """
    X = df.drop(columns=[target])
    y = df[target]
    return model_selection.train_test_split(X, y, test_size=test_size,
                                            random_state=random_state,
                                            stratify=y)
