import matplotlib
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler


# ===============================
# Step 1: Create Sample Dataset
# ===============================

np.random.seed(42)

data = {
    "Age": np.random.randint(20, 50, 100),
    "Salary": np.random.randint(20000, 200000, 100)
}

df = pd.DataFrame(data)

print("Original Data (First 5 rows):")
print(df.head())


# ===============================
# Step 2: Standardization
# (Mean = 0, Std = 1)
# ===============================

standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data (First 5 rows):")
print(df_standardized.head())


# ===============================
# Step 3: Normalization
# (Range 0 to 1)
# ===============================

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data (First 5 rows):")
print(df_normalized.head())


# ===============================
# Step 4: Plot Histogram (Salary)
# ===============================

plt.figure()
plt.hist(df["Salary"])
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.savefig("salary_original.png")

plt.figure()
plt.hist(df_standardized["Salary"])
plt.title("Standardized Salary Distribution")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.savefig("salary_standardized.png")

plt.figure()
plt.hist(df_normalized["Salary"])
plt.title("Normalized Salary Distribution")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.savefig("salary_normalized.png")

print("\nHistograms saved as:")
print("salary_original.png")
print("salary_standardized.png")
print("salary_normalized.png")
