import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(r"D:\house\dataset\Luxury_Housing_Cleaned.csv")

print("Cleaned data loaded successfully")
print("Shape:", df.shape)
print("Columns:", list(df.columns))

# Possession Status Distribution

plt.figure(figsize=(8, 5))
sns.countplot(
    x='Possession_Status',
    hue='Possession_Status',
    data=df,
    palette='Set2',
    legend=False
)

plt.title('Distribution of Possession Status')
plt.xlabel('Possession Status')
plt.ylabel('Number of Properties')
plt.tight_layout()
plt.show()

# Unit Size vs Ticket Price
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x='Unit_Size_Sqft',
    y='Ticket_Price_Cr',
    hue='Configuration',
    data=df,
    alpha=0.6
)
plt.title('Unit Size vs Ticket Price by Configuration')
plt.xlabel('Unit Size (Sqft)')
plt.ylabel('Ticket Price (Cr)')
plt.tight_layout()
plt.show()

# Correlation Heatmap
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

plt.figure(figsize=(10, 6))
corr = df[numeric_cols].corr()
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    linewidths=0.5
)
plt.title('Correlation Between Numeric Features')
plt.tight_layout()
plt.show()

# Price Distribution by Configuration

plt.figure(figsize=(8, 5))
sns.boxplot(
    x='Configuration',
    y='Ticket_Price_Cr',
    data=df,
    palette='Set3'
)
plt.title('Ticket Price Distribution by Configuration')
plt.xlabel('Configuration')
plt.ylabel('Ticket Price (Cr)')
plt.tight_layout()
plt.show()

print("EDA completed successfully")
