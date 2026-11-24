#!/usr/bin/env python3
"""Create an ordinary least squares linear regression model."""
from sklearn import linear_model


def Linear_Regression():
    """Return an untrained scikit-learn LinearRegression model.

    The model uses ordinary least squares to fit a linear model.
    """
    model = linear_model.LinearRegression()
    return model
