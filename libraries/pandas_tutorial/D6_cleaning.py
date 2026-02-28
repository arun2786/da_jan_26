import pandas as pd

# Step 3: Load
df = pd.read_csv("real_data.csv")

# Step 4: Inspect
print(df.isnull().sum())

# Step 5: Remove duplicates
df = df.drop_duplicates()

# Step 6: Handle missing text columns
df["department"] = df["department"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")
df["email"] = df["email"].fillna("not_provided@company.com")
df = df.dropna(subset=["name"])

# Step 7: Handle missing numeric columns
df["salary"] = df["salary"].fillna(df["salary"].median())
df["joining_date"] = df["joining_date"].fillna("2000-01-01")

# Step 8: Fix inconsistent text
df["department"] = df["department"].str.strip().str.upper()

# Step 9: Verify
print(df.isnull().sum())
print(df.shape)

# Step 10: Save
df.to_csv("employees_cleaned.csv", index=False)
print("Done.")

