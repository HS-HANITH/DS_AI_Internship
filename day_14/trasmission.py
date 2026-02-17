import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ===============================
# Step 1: Create Dataset
# ===============================

data = {
    "Transmission": ["Automatic", "Manual", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Blue", "Red"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# ===============================
# Step 2: Label Encoding (Binary Column)
# ===============================

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print("\nAfter Label Encoding (Transmission):")
print(df)


# ===============================
# Step 3: One-Hot Encoding (Nominal Column)
# ===============================

df_encoded = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter One-Hot Encoding (Color):")
print(df_encoded)
