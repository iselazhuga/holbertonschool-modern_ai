#!/usr/bin/env python3
"""Plot how many customers churned and how many stayed."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Draw a bar plot of the counts of each Churn value.

    'No' is drawn in skyblue and 'Yes' in salmon.
    """
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    colors = ['skyblue' if value == 'No' else 'salmon'
              for value in counts.index]
    plt.bar(counts.index, counts.values, color=colors)
    plt.title("Churn Distribution")
    plt.ylabel("Count")
    plt.show()
