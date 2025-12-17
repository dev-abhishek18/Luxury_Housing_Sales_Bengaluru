import pandas as pd
from sqlalchemy import create_engine, text

print("START")

df = pd.read_csv(r"D:\house\dataset\Luxury_Housing_Cleaned.csv")
print("CSV loaded, rows =", len(df))

# CLEAN & FORCE NUMERIC
numeric_cols = [
    "Unit_Size_Sqft",
    "Ticket_Price_Cr",
    "Connectivity_Score",
    "Amenity_Score",
    "Locality_Infra_Score",
    "Avg_Traffic_Time_Min"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("â‚¹", "", regex=False)
            .str.replace("Cr", "", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

df["Purchase_Quarter"] = pd.to_datetime(df["Purchase_Quarter"], errors="coerce")

print("Numeric & date conversion DONE")

# SQL CONNECTION
engine = create_engine(
    "mssql+pyodbc://sa:ISS@DESKTOP-NSAHO9N\\SQLSERVER2019/LuxuryHousing_db"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))
print("SQL connection OK")

# INSERT DATA (SAFE MODE)
df.to_sql(
    name="HousingData",
    con=engine,
    schema="dbo",
    if_exists="append",
    index=False
)

print("FULL DATA INSERTED SUCCESSFULLY")
input("Press ENTER to close...")
