import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Before Cleaning:\n", df["Location"].unique())

df["Location"] = df["Location"].astype(str)

df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()

print("\nAfter Cleaning:\n", df["Location"].unique())
