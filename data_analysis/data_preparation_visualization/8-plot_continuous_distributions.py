#!/usr/bin/env python3
"""Plot the distributions of continuous numeric columns."""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Draw a histogram with KDE and a box plot for each numeric column.

    df is a pandas DataFrame. columns_to_plot is a list of numeric
    columns; when it is None every numeric column is used.
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=np.number).columns.tolist()

    n_cols = len(columns_to_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()
        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                        edgecolor='black')
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 200)
        axes[i, 0].plot(x, kde(x), color='red', linestyle='--')
        axes[i, 0].set_title(f"{col} Histogram + KDE")
        axes[i, 1].boxplot(data, orientation='horizontal')
        axes[i, 1].set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
