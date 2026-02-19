import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# 1️⃣ Generate Equal-Length Data
# ---------------------------------

np.random.seed(42)

size = 1002  # Same size for all columns

heights = np.random.normal(loc=170, scale=10, size=size)
incomes = np.random.exponential(scale=50000, size=size)
scores = 100 - np.random.exponential(scale=10, size=size)

# Create DataFrame (NO length mismatch)
data = pd.DataFrame({
    "Heights (Normal)": heights,
    "Incomes (Right-Skewed)": incomes,
    "Scores (Left-Skewed)": scores
})

# ---------------------------------
# 2️⃣ Analysis Function
# ---------------------------------

def analyze_distribution(column, title):

    mean = column.mean()
    median = column.median()
    std_dev = column.std()

    print("\n===================================")
    print(title)
    print("===================================")
    print(f"Mean (μ): {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation (σ): {std_dev:.2f}")

    # Skew Detection
    if mean > median:
        print("Skew Type: Right-Skewed")
    elif mean < median:
        print("Skew Type: Left-Skewed")
    else:
        print("Skew Type: Approximately Normal")

    # Z-Score Calculation
    data["z_score"] = (column - mean) / std_dev

    # Outlier Detection
    outliers = data[np.abs(data["z_score"]) > 3]
    print(f"Number of Outliers (|Z| > 3): {len(outliers)}")

    # Plot Histogram + KDE
    plt.figure(figsize=(6,4))
    sns.histplot(column, bins=30, kde=True)
    plt.title(title)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.tight_layout()



analyze_distribution(data["Heights (Normal)"], "Human Heights (Normal)")
analyze_distribution(data["Incomes (Right-Skewed)"], "Household Incomes (Right-Skewed)")
analyze_distribution(data["Scores (Left-Skewed)"], "Easy Exam Scores (Left-Skewed)")

plt.show()
