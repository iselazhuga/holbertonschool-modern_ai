#!/usr/bin/env python3
"""Plot a correlation heatmap of the numeric columns."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Draw an annotated heatmap of the correlations between numeric columns.

    Colours run from -1 (blue) to 1 (red) with the coolwarm colormap.
    """
    plt.figure(figsize=(6, 5))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.savefig("Task_9.png")
    plt.show()
