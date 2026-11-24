#!/usr/bin/env python3
"""Compute common evaluation metrics for a regression model."""
from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    """Return the MSE, RMSE, MAE and R squared of the predictions.

    Args:
        y_true: 1D numpy array with the true target values.
        y_pred: 1D numpy array with the predicted target values.

    Returns:
        A tuple (mse, rmse, mae, r2).
    """
    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)
    return mse, rmse, mae, r2
