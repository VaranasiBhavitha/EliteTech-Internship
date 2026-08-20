import pandas as pd
from sklearn.preprocessing import StandardScaler
# -----------------------------------------
# 1. EXTRACT
# -----------------------------------------

# Load raw data from CSV
df = pd.read_csv("data/raw_data.csv")

print("Raw Data:")
print(df)
# -----------------------------------------
# 2. PREPROCESSING
# -----------------------------------------

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age with the median Age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks with the median Marks
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Remove duplicate records
df = df.drop_duplicates()
# -----------------------------------------
# 3. TRANSFORMATION
# -----------------------------------------

# Standardize Age and Marks
scaler = StandardScaler()

df[["Age", "Marks"]] = scaler.fit_transform(
    df[["Age", "Marks"]]
)
# -----------------------------------------
# 4. LOAD
# -----------------------------------------

# Save the processed data
df.to_csv("data/processed_data.csv", index=False)
# -----------------------------------------
# 5. OUTPUT
# -----------------------------------------

print("\nProcessed Data:")
print(df)

print("\nPipeline completed successfully!")