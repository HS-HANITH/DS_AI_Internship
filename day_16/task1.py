import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# -------------------------------
# 1️⃣ Generate Datasets
# -------------------------------

# Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Income)
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Create DataFrame
data = pd.DataFrame({
    "Heights (Normal)": heights,
    "Incomes (Right-Skewed)": incomes,
    "Scores (Left-Skewed)": scores
})

# -------------------------------
# 2️⃣ Function to Analyze Data
# -------------------------------

def analyze_distribution(column, title):
    mean = column.mean()
    median = column.median()

    print(f"\n--- {title} ---")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")

    if mean > median:
        print("Skew Type: Right-Skewed")
    elif mean < median:
        print("Skew Type: Left-Skewed")
    else:
        print("Skew Type: Approximately Normal")

    # Plot Histogram + KDE
    plt.figure()
    sns.histplot(column, kde=True)
    plt.title(title)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()

# -------------------------------
# 3️⃣ Analyze Each Dataset
# -------------------------------

analyze_distribution(data["Heights (Normal)"], "Human Heights (Normal)")
analyze_distribution(data["Incomes (Right-Skewed)"], "Household Incomes (Right-Skewed)")
analyze_distribution(data["Scores (Left-Skewed)"], "Easy Exam Scores (Left-Skewed)")
