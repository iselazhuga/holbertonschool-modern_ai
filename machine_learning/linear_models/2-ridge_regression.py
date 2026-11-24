#!/usr/bin/env python3
"""Create a Ridge regression model (linear regression with L2 penalty)."""
from sklearn import linear_model


def ridge_regression(random_state):
    """Return an untrained scikit-learn Ridge regression model.

    Ridge adds L2 regularisation to ordinary least squares, shrinking
    large coefficients to make the model more stable.

    Args:
        random_state: integer seed for reproducibility.

    Returns:
        An untrained Ridge model.
    """
    model = linear_model.Ridge(random_state=random_state)
    return model
