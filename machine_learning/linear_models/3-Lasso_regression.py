#!/usr/bin/env python3
"""Create a Lasso regression model (linear regression with L1 penalty)."""
from sklearn import linear_model


def lasso_regression(random_state):
    """Return an untrained scikit-learn Lasso regression model.

    Lasso adds L1 regularisation to ordinary least squares, which can
    shrink some coefficients exactly to zero and so selects features.

    Args:
        random_state: integer seed for reproducibility.

    Returns:
        An untrained Lasso model.
    """
    model = linear_model.Lasso(random_state=random_state)
    return model
