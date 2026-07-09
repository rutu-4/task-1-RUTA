import pandas as pd

df = pd.read_excel("orders.xlsx")

# Check missing values
print(df.isnull().sum())

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Check duplicates
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())

# Fix date format and check invalid dates
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print("Invalid dates:", df["Date"].isnull().sum())

# Convert date to standard format YYYY-MM-DD
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Save cleaned dataset
df.to_excel("cleaned_orders.xlsx", index=False)

print("Cleaned file saved successfully!")