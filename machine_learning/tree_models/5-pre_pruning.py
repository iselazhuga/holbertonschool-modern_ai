#!/usr/bin/env python3
"""Find the best pre-pruning hyperparameters for a decision tree."""
from sklearn import model_selection


def prepruning(X, y, clf):
    """Grid search the pre-pruning hyperparameters of a decision tree.

    The search explores criterion ("gini" or "entropy") and max_depth,
    min_samples_leaf and min_samples_split in the range [2, 5).

    Args:
        X: input features.
        y: target labels.
        clf: an untrained DecisionTreeClassifier.

    Returns:
        A dictionary with the best combination of hyperparameters.
    """
    param_grid = {
        "criterion": ["gini", "entropy"],
        "max_depth": list(range(2, 5)),
        "min_samples_leaf": list(range(2, 5)),
        "min_samples_split": list(range(2, 5)),
    }
    search = model_selection.GridSearchCV(clf, param_grid)
    search.fit(X, y)
    return search.best_params_
