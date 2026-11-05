#!/usr/bin/env python3
"""Plot where the missing values of a DataFrame are."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Draw a mark for every missing value of df.

    The x-axis is the row index and the y-axis is the column name.
    """
    plt.figure(figsize=(12, 8))

    rows, cols = np.where(df.isnull())
    plt.scatter(rows, cols, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title("Missingness Plot")

    plt.tight_layout()
    plt.show()
