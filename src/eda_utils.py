import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def summarize_data(df):
    """
    Return summary statistics.
    """
    return df.describe()


def missing_values(df):
    """
    Return missing value counts.
    """
    return df.isnull().sum()


def plot_histogram(df, column):
    """
    Plot histogram.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()


def plot_boxplot(df, column):
    """
    Plot boxplot.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()