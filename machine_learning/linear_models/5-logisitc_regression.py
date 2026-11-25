#!/usr/bin/env python3
"""Create a logistic regression model for binary classification."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Return an untrained scikit-learn LogisticRegression model.

    Logistic regression passes a linear score through the logistic
    (sigmoid) function to get a probability for binary classification.

    Args:
        random_state: integer seed for reproducibility.

    Returns:
        An untrained LogisticRegression model.
    """
    model = linear_model.LogisticRegression(random_state=random_state)
    return model
