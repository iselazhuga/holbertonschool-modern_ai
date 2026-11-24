#!/usr/bin/env python3
"""Explain a trained regression model with SHAP values."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Create a SHAP explainer and compute SHAP values for X_test.

    Args:
        model: a trained regression model.
        X_train: data used as the background for the explainer.
        X_test: data whose predictions are explained.

    Returns:
        A tuple (explainer, shap_values).
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
