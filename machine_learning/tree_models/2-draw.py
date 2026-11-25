#!/usr/bin/env python3
"""Print the decision rules of a trained decision tree."""
from sklearn import tree


def draw(clf, feature_names, class_names):
    """Print a readable text representation of a trained decision tree.

    Args:
        clf: a trained DecisionTreeClassifier.
        feature_names: list of the input feature names.
        class_names: list of the target class names.

    Returns:
        None
    """
    rules = tree.export_text(clf,
                             feature_names=list(feature_names),
                             class_names=list(class_names))
    print(rules)
