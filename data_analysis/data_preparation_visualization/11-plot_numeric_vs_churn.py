#!/usr/bin/env python3
"""Compare the distribution of a numeric column for each Churn value."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Draw the histograms of col for Churn 'No' and 'Yes' side by side."""
    plt.figure(figsize=(12, 8))
    stayed = df.loc[df['Churn'] == 'No', col]
    churned = df.loc[df['Churn'] == 'Yes', col]
    plt.hist([stayed, churned], bins=30, label=['No', 'Yes'])
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
