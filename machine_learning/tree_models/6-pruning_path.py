#!/usr/bin/env python3
"""Retrieve the cost-complexity pruning path of a decision tree."""


def get_pruning_path(clf, X, y):
    """Return the effective alphas and leaf impurities of the pruning path.

    Args:
        clf: a DecisionTreeClassifier instance.
        X: input features.
        y: target labels.

    Returns:
        A tuple (ccp_alphas, impurities) of numpy arrays: the effective
        alphas used for pruning and the total leaf impurity at each one.
    """
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities
