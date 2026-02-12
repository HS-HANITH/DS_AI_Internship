import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "customer_orders.csv"

if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    raise FileNotFoundError("Dataset not found. Expected 'customer_orders.csv'.")

print("Shape before cleaning:", df.shape)

print("Missing values per column:")
print(df.isna().sum())

numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df_cleaned = df.drop_duplicates()

print("Shape after cleaning:", df_cleaned.shape)