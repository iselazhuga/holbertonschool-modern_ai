#!/usr/bin/env python3
"""Select the best ccp_alpha for a set of pruned decision trees."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Return the best ccp_alpha and its trained classifier.

    The best model has the highest test accuracy. Ties are broken by
    the smallest gap between train and test accuracy, then by the
    largest ccp_alpha (the simpler, more regularised tree).

    Args:
        clfs: list of trained DecisionTreeClassifier instances.
        train_scores: training accuracy of each classifier.
        test_scores: test accuracy of each classifier.
        ccp_alphas: ccp_alpha used to train each classifier.

    Returns:
        A tuple (best_alpha, best_clf).
    """
    best_test = max(test_scores)
    candidates = [i for i in range(len(clfs))
                  if test_scores[i] == best_test]
    best = min(candidates,
               key=lambda i: (abs(train_scores[i] - test_scores[i]),
                              -ccp_alphas[i]))
    return ccp_alphas[best], clfs[best]
