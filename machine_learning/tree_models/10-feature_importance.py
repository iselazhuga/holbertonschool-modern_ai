#!/usr/bin/env python3
"""Compute the feature importances of a trained random forest."""
import numpy as np


def feature_importance(rf):
    """Return the feature importances and their indices in ascending order.

    Args:
        rf: a trained scikit-learn RandomForestClassifier.

    Returns:
        A tuple (importances, indices): the importance score of each
        feature, and the feature indices sorted from least to most
        important.
    """
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
