from pathlib import Path
print("RUNNING FILE:", Path(__file__).resolve())

BASE_DIR = Path(__file__).resolve().parent.parent
print("BASE DIR:", BASE_DIR)
print("DATA DIR EXISTS:", (BASE_DIR / "data").exists())
print("FILES IN DATA:", list((BASE_DIR / "data").iterdir()))


import pandas as pd
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load data
data_path = BASE_DIR / "data" / "superstore_raw.csv"
df = pd.read_csv(data_path, encoding="latin1")


# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Create new columns
df['Order_Year'] = df['Order Date'].dt.year
df['Order_Month'] = df['Order Date'].dt.month
df['Profit_Margin'] = df['Profit'] / df['Sales']

# Save cleaned data
output_path = BASE_DIR / "data" / "superstore_cleaned.csv"
df.to_csv(output_path, index=False)

print("Data cleaning completed successfully")
