#!/usr/bin/env python3
"""Create a support vector machine classifier with a chosen kernel."""
from sklearn import svm


def get_SVM_model(name, random_state):
    """Return an untrained scikit-learn SVC with the given kernel.

    Args:
        name: kernel type, one of 'linear', 'poly' or 'rbf'.
        random_state: integer seed for reproducibility.

    Returns:
        An untrained SVC model.
    """
    model = svm.SVC(kernel=name, random_state=random_state)
    return model
