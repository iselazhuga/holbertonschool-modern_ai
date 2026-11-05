#!/usr/bin/env python3
"""Plot the distributions of categorical columns."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Draw a bar plot of the value counts of each categorical column.

    columns_to_plot is a list of columns; when it is None every column of
    dtype object except the target Churn is used. Plots go in a grid of
    3 columns and unused cells are removed.
    """
    if columns_to_plot is None:
        columns = [col for col in df.select_dtypes(include='object').columns
                   if col != 'Churn']
    else:
        columns = list(columns_to_plot)
    n_cols, n_rows = 3, (len(columns) + 2) // 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    axes = axes.flatten()
    for ax, col in zip(axes, columns):
        counts = df[col].value_counts()
        ax.bar(counts.index, counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)
    for ax in axes[len(columns):]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
