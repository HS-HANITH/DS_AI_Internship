# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Set Random Seed
# -----------------------------
np.random.seed(42)

# -----------------------------
# Step 2: Create Dataset (500 rows)
# -----------------------------
n = 500

square_footage = np.random.randint(500, 4000, n)
bedrooms = square_footage // 500   # strongly related to square footage
bathrooms = bedrooms - 1 + np.random.randint(0, 2, n)
price = square_footage * 3000 + np.random.normal(0, 500000, n)

df = pd.DataFrame({
    "SquareFootage": square_footage,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Price": price
})

# -----------------------------
# Step 3: Correlation Matrix
# -----------------------------
correlation_matrix = df.corr()

print("Correlation Matrix:\n")
print(correlation_matrix)

# -----------------------------
# Step 4: Heatmap Visualization
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# Step 5: Identify High Correlation (>0.8)
# -----------------------------
print("\nHighly Correlated Pairs (>0.8):")

for col1 in correlation_matrix.columns:
    for col2 in correlation_matrix.columns:
        if col1 != col2:
            corr_value = correlation_matrix.loc[col1, col2]
            if abs(corr_value) > 0.8:
                print(f"{col1} and {col2} --> {corr_value}")

# -----------------------------
# Step 6: Boxplot for Outliers (Price)
# -----------------------------
plt.figure(figsize=(6,5))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price")
plt.show()
