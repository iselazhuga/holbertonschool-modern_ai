#!/usr/bin/env python3
"""Create a decision tree classifier."""
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """Return an untrained DecisionTreeClassifier using Gini impurity.

    No maximum depth is set, so the tree grows until its leaves are
    pure or the other stopping criteria are met.

    Args:
        min_samples_leaf: minimum number of samples required at a leaf.
        min_samples_split: minimum number of samples required to split
            an internal node.
        random_state: integer seed for reproducibility.

    Returns:
        A DecisionTreeClassifier instance.
    """
    model = tree.DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state)
    return model
