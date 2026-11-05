#!/usr/bin/env python3
"""Plot the churn rate of each category of a column."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Draw a bar plot of the share of 'Yes' churn for each value of col."""
    plt.figure(figsize=(12, 8))
    churn_rate = (df['Churn'] == 'Yes').groupby(df[col]).mean()
    plt.bar(churn_rate.index, churn_rate.values)
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.show()
