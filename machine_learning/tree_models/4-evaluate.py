#!/usr/bin/env python3
"""Evaluate a classifier with a classification report."""
from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """Return the scikit-learn classification report as a string.

    The report shows precision, recall and F1-score for every class.

    Args:
        true_labels: ground truth labels.
        predicted_labels: predicted labels.
        class_names: class names matching the label indices.

    Returns:
        A string with the classification report.
    """
    return metrics.classification_report(true_labels,
                                         predicted_labels,
                                         target_names=class_names)
