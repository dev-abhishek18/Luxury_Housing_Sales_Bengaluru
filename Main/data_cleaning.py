import pandas as pd
import numpy as np

print("START DATA CLEANING")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"D:\house\dataset\Luxury_Housing_Bangalore.csv")
print("CSV Loaded | Rows:", len(df))

# ---------------- REMOVE DUPLICATES ----------------
df.drop_duplicates(inplace=True)
print("Duplicates Removed | Rows:", len(df))

# ---------------- FIX TICKET_PRICE_CR ----------------
def clean_price(value):
    if pd.isna(value):
        return np.nan

    value = str(value)

    value = value.replace("â‚¹", "").replace("₹", "")
    value = value.replace("Cr", "").replace("CR", "")
    value = value.replace(",", "").strip()

    try:
        return float(value)
    except:
        return np.nan

df["Ticket_Price_Cr"] = df["Ticket_Price_Cr"].apply(clean_price)

# ---------------- DATE CONVERSION ----------------
df["Purchase_Quarter"] = pd.to_datetime(
    df["Purchase_Quarter"], errors="coerce"
)

# ---------------- NUMERIC COLUMNS ----------------
numeric_cols = [
    "Unit_Size_Sqft",
    "Connectivity_Score",
    "Amenity_Score",
    "Locality_Infra_Score",
    "Avg_Traffic_Time_Min"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------- AMENITY_SCORE → MEDIAN ----------------
amenity_median = df["Amenity_Score"].median()
df["Amenity_Score"].fillna(amenity_median, inplace=True)
print("Amenity_Score filled with MEDIAN:", amenity_median)


# ---------------- BUYER_COMMENTS ----------------
df["Buyer_Comments"] = (
    df["Buyer_Comments"]
    .replace(["", " ", "nan", "NaN", None], pd.NA)
    .fillna("No Comments")
    .astype(str)
)



# ---------------- SAVE CLEAN DATA ----------------
output_path = r"D:\house\dataset\Luxury_Housing_Cleaned.csv"
df.to_csv(output_path, index=False)

print("DATA CLEANING COMPLETED")
print("Clean file saved at:", output_path)
print("FINAL SHAPE:", df.shape)
