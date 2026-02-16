# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Set Random Seed
# -------------------------------
np.random.seed(42)

# -------------------------------
# Step 2: Create Random Dataset (500 rows)
# -------------------------------
n = 500

square_footage = np.random.randint(500, 4000, n)

# Price depends on square footage + some randomness
price = square_footage * 3000 + np.random.normal(0, 500000, n)

data = pd.DataFrame({
    "SquareFootage": square_footage,
    "Price": price,
    "City": np.random.choice(["Bangalore", "Mumbai", "Delhi", "Chennai"], n)
})

# -------------------------------
# Step 3: Scatter Plot
# -------------------------------
plt.figure(figsize=(7,5))
sns.scatterplot(x="SquareFootage", y="Price", data=data)
plt.title("SquareFootage vs Price")
plt.show()

# -------------------------------
# Step 4: Boxplot (Categorical vs Numerical)
# -------------------------------
plt.figure(figsize=(7,5))
sns.boxplot(x="City", y="Price", data=data)
plt.title("City vs Price Distribution")
plt.show()

# -------------------------------
# Step 5: Observation
# -------------------------------
print("Observation:")
print("As SquareFootage increases, Price seems to increase.")
