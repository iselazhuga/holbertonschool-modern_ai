#!/usr/bin/env python3
"""Create a random forest classifier."""
from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """Return an untrained scikit-learn RandomForestClassifier.

    Args:
        n_estimators: number of trees in the forest.
        random_state: integer seed for reproducibility.

    Returns:
        A RandomForestClassifier instance.
    """
    model = ensemble.RandomForestClassifier(n_estimators=n_estimators,
                                            random_state=random_state)
    return model
