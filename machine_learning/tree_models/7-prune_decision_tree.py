#!/usr/bin/env python3
"""Train and evaluate decision trees over a range of ccp_alpha values."""
from sklearn import tree
train_tree = __import__('1-train').train_tree


def prune_and_evaluate_trees(X_train, y_train, X_test, y_test, ccp_alphas,
                             random_state, min_samples_leaf,
                             min_samples_split):
    """Train one pruned decision tree per ccp_alpha and score each one.

    Args:
        X_train: training features.
        y_train: training labels.
        X_test: testing features.
        y_test: testing labels.
        ccp_alphas: numpy array of cost-complexity pruning alphas.
        random_state: integer seed for reproducibility.
        min_samples_leaf: minimum number of samples required at a leaf.
        min_samples_split: minimum number of samples required to split
            an internal node.

    Returns:
        A tuple (clfs, train_scores, test_scores): the trained trees and
        their training and testing accuracy, one per ccp_alpha.
    """
    clfs = []
    train_scores = []
    test_scores = []
    for ccp_alpha in ccp_alphas:
        clf = tree.DecisionTreeClassifier(
            random_state=random_state,
            min_samples_leaf=min_samples_leaf,
            min_samples_split=min_samples_split,
            ccp_alpha=ccp_alpha)
        train_tree(clf, X_train, y_train)
        clfs.append(clf)
        train_scores.append(float(clf.score(X_train, y_train)))
        test_scores.append(float(clf.score(X_test, y_test)))
    return clfs, train_scores, test_scores
