import pandas as pd

df = pd.read_csv("real_data.csv")
print(df)
print("\nShape:", df.shape)


""" Before cleaning, always explore the data first. """

# View basic info - column names, data types, non-null counts
print(df.info())

# Count missing values in each column
print("\nMissing Values:\n", df.isnull().sum())



""" Remove Duplicate Rows """
# Row with emp_id = 101 (Suresh) appears twice.
print("Before removing duplicates:", df.shape)

df = df.drop_duplicates()

print("After removing duplicates:", df.shape)



""" Handle Missing Values in Text Columns """
# Fill with a default value
df["department"] = df["department"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")
df["email"] = df["email"].fillna("not_provided@company.com")

# Drop rows where a critical column is empty
df = df.dropna(subset=["name"])


""" Handle Missing Values in Numeric Columns """
# Fill with the column average (mean)
avg_salary = df["salary"].mean()
df["salary"] = df["salary"].fillna(avg_salary)
print("Average salary used for fill:", avg_salary)

# For the date column, fill with a placeholder date:
df["joining_date"] = df["joining_date"].fillna("2000-01-01")

""" Fix Inconsistent Text Values """
# standardize all department names.
df["department"] = df["department"].str.strip().str.upper()
print(df["department"].unique())


""" Verify the Clean Data """
print("\nCleaned Data:\n")
print(df.to_string(index=False))

print("\nMissing values after cleaning:\n", df.isnull().sum())
print("\nFinal shape:", df.shape)


""" Save the Cleaned Data to a New CSV """
df.to_csv("employees_cleaned.csv", index=False)
print("Cleaned file saved as employees_cleaned.csv")


