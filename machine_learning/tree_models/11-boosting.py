#!/usr/bin/env python3
"""Create an untrained boosting classifier chosen by name."""
from sklearn import ensemble
import xgboost as xgb
import lightgbm as lgb


def compare_boosting_classifiers(name, n_estimators, random_state):
    """Return an untrained boosting classifier for the given algorithm.

    Args:
        name: one of 'adaboost', 'gradientboosting', 'xgboost' or
            'lightgbm'.
        n_estimators: number of boosting iterations (trees).
        random_state: integer seed for reproducibility.

    Returns:
        An untrained instance of the selected boosting classifier.

    Raises:
        ValueError: if name is not one of the supported algorithms.
    """
    if name == "adaboost":
        return ensemble.AdaBoostClassifier(n_estimators=n_estimators,
                                           random_state=random_state)
    if name == "gradientboosting":
        return ensemble.GradientBoostingClassifier(
            n_estimators=n_estimators, random_state=random_state)
    if name == "xgboost":
        return xgb.XGBClassifier(n_estimators=n_estimators,
                                 random_state=random_state)
    if name == "lightgbm":
        return lgb.LGBMClassifier(n_estimators=n_estimators,
                                  random_state=random_state,
                                  verbose=-1)
    raise ValueError(f"Unknown model name '{name}'")
