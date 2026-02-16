# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# -------------------------------
# Step 1: Set Random Seed
# -------------------------------
np.random.seed(42)

# -------------------------------
# Step 2: Generate Random Dataset (500 rows)
# -------------------------------
n = 500

data = pd.DataFrame({
    "Price": np.random.lognormal(mean=15, sigma=0.5, size=n),  # Skewed prices
    "City": np.random.choice(["Bangalore", "Mumbai", "Delhi", "Chennai"], size=n)
})

# -------------------------------
# Step 3: Plot Histogram + KDE
# -------------------------------
plt.figure(figsize=(8,5))
sns.histplot(data["Price"], kde=True)
plt.title("Histogram with KDE of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# Step 4: Calculate Skewness & Kurtosis
# -------------------------------
price_skewness = skew(data["Price"])
price_kurtosis = kurtosis(data["Price"])

print("Skewness of Price:", price_skewness)
print("Kurtosis of Price:", price_kurtosis)

# -------------------------------
# Step 5: Count Plot for Categorical Column
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="City", data=data)
plt.title("Count Plot of City")
plt.show()
