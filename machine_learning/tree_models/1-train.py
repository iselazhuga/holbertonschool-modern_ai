#!/usr/bin/env python3
"""Train a tree-based classifier."""


def train_tree(clf, X, y):
    """Fit a scikit-learn classifier on the given data, in place.

    Args:
        clf: a scikit-learn classifier instance.
        X: input features.
        y: target labels.

    Returns:
        None
    """
    clf.fit(X, y)
