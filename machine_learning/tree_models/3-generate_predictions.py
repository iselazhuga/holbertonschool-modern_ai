#!/usr/bin/env python3
"""Generate predictions from a trained tree-based classifier."""


def generate_predictions(clf, X):
    """Return the predicted class labels for the samples in X.

    Args:
        clf: a trained scikit-learn classifier.
        X: feature matrix (numpy array or pandas DataFrame).

    Returns:
        A numpy array with the predicted class labels.
    """
    return clf.predict(X)
