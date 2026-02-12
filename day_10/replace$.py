import pandas as pd

df = pd.read_csv("customer_orders.csv")

df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns.tolist())


df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)

df["date"] = pd.to_datetime(df["date"])

print("\nUpdated Data Types:\n", df.dtypes)
