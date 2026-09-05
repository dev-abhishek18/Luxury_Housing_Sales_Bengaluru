# Luxury Housing Sales Analysis – Bengaluru

> **End-to-end Data Analytics project using Python, SQL Server and Power BI to analyze luxury residential housing sales in Bengaluru.**

## 📌 Project Overview

This project demonstrates a complete **Data Analyst workflow** starting from raw real-estate data and progressing through data cleaning, exploratory analysis, SQL-based data loading, and business-focused dashboarding.

The project is designed to answer practical business questions around:

- Market and locality performance
- Builder performance
- Property pricing
- Configuration demand
- Buyer behavior
- Property amenities and connectivity
- Possession status
- Sales trends

The dataset contains **100,000+ property records**, making the project suitable for demonstrating large-scale data preparation and analytical workflows.

---

## 🎯 Business Problem

Real-estate stakeholders need to understand **where demand is strongest, which builders and configurations perform better, how property attributes relate to price, and how market activity changes over time**.

The objective of this project is to transform raw housing-sales data into a structured analytical dataset and generate insights that can support:

- Market strategy
- Pricing decisions
- Builder benchmarking
- Product/configuration planning
- Buyer segmentation
- Sales performance monitoring

---

## 🔎 Key Analytical Questions

1. Which micro-markets have the highest property activity?
2. Which developers generate higher sales value and average ticket prices?
3. How does unit size relate to ticket price?
4. Which configurations are most in demand?
5. How does ticket price vary across configurations?
6. What is the distribution of possession status across properties?
7. How do amenity, connectivity and infrastructure scores relate to property performance?
8. How does booking activity change across purchase quarters?
9. How do buyer types and sales channels differ across the market?
10. Which property segments should receive greater business attention?

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Data Cleaning | Python, Pandas, NumPy |
| Exploratory Data Analysis | Pandas, Matplotlib, Seaborn |
| Database | Microsoft SQL Server |
| Python–SQL Integration | SQLAlchemy, PyODBC |
| Visualization | Power BI |
| Version Control | Git, GitHub |

---

## 📊 Dataset

**Dataset:** `Luxury_Housing_Bangalore.csv`

**Cleaned Dataset:** `Luxury_Housing_Cleaned.csv`

**Scale:** 100,000+ records

### Important fields

- `Property_ID`
- `Micro_Market`
- `Project_Name`
- `Developer_Name`
- `Unit_Size_Sqft`
- `Configuration`
- `Ticket_Price_Cr`
- `Transaction_Type`
- `Buyer_Type`
- `Purchase_Quarter`
- `Amenity_Score`
- `Connectivity_Score`
- `Locality_Infra_Score`
- `Avg_Traffic_Time_Min`
- `Possession_Status`
- `Sales_Channel`
- `NRI_Buyer`
- `Buyer_Comments`

---

## 🔄 End-to-End Data Workflow

```text
Raw CSV Dataset
      ↓
Python Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Cleaned CSV Dataset
      ↓
SQL Server
      ↓
Business Analysis
      ↓
Power BI Dashboard
      ↓
Business Insights
```

### 1. Python – Data Cleaning

The `Main/data_cleaning.py` script prepares the raw dataset for analysis.

Key data-preparation steps include:

- Load raw CSV data using Pandas
- Remove duplicate records
- Clean currency/price values containing `₹` and `Cr`
- Convert numeric fields to appropriate numeric types
- Convert `Purchase_Quarter` into a date field
- Handle missing `Amenity_Score` values using the **median**
- Replace missing buyer comments with `No Comments`
- Export the cleaned dataset for downstream analysis

This creates a consistent analytical dataset before database loading.

### 2. Exploratory Data Analysis

The `Main/eda_analysis.py` script performs exploratory analysis using Pandas, Matplotlib and Seaborn.

Analysis includes:

- Possession-status distribution
- Unit size vs. ticket price analysis
- Configuration-level price distribution
- Correlation analysis between numeric variables
- Distribution and relationship analysis across property attributes

### 3. SQL Server – Data Loading

The `Main/load_to_sql.py` script loads the cleaned dataset into SQL Server.

The workflow includes:

- Read the cleaned dataset
- Standardize numeric and date fields
- Establish a SQL Server connection through SQLAlchemy/PyODBC
- Validate the database connection
- Load the analytical data into the `HousingData` table

### 4. Power BI – Business Dashboard

Power BI is used as the visualization and business-analysis layer.

The dashboard is designed around interactive analysis of:

- Builder performance
- Micro-market performance
- Configuration demand
- Purchase-quarter trends
- Possession status
- Buyer type
- Pricing and property characteristics

---

## 📈 Dashboard Analysis Areas

The project focuses on business-friendly KPIs and visual analysis such as:

- Total properties
- Total sales value / revenue
- Average ticket price
- Average amenity score
- Quarterly sales/booking trends
- Builder-wise performance
- Configuration demand
- Amenity and property-feature relationships

Interactive filters help users move from a high-level market view to specific builders, locations, configurations and buyer segments.

---

## 💡 Business Insights

The analysis is designed to identify patterns such as:

- Differences in performance between Bengaluru micro-markets
- Variation in pricing across property configurations
- Demand concentration across major configurations
- Relationship between property size and ticket price
- Differences in property characteristics across possession statuses
- Correlation patterns among numeric property and locality attributes
- Changes in market activity across purchase periods

> **Note:** The README intentionally avoids fabricated numerical claims. Exact KPI values should be taken directly from the dataset/dashboard rather than hard-coded into project documentation.

---

## 🧠 Data Analyst Skills Demonstrated

This project demonstrates practical skills relevant to a **Data Analyst role**:

- Data cleaning and preprocessing
- Missing-value handling
- Duplicate detection and removal
- Data-type standardization
- Exploratory Data Analysis (EDA)
- Descriptive analytics
- Correlation analysis
- Business problem framing
- KPI identification
- SQL Server data handling
- Python–SQL integration
- Dashboard development
- Business insight generation
- Data storytelling
- Git/GitHub project documentation

---

## 📁 Project Structure

```text
Luxury_Housing_Sales_Bengaluru/
│
├── Main/
│   ├── data_cleaning.py       # Data cleaning & preprocessing
│   ├── eda_analysis.py        # Exploratory Data Analysis
│   └── load_to_sql.py         # Load cleaned data into SQL Server
│
├── dataset/
│   ├── Luxury_Housing_Bangalore.csv
│   └── Luxury_Housing_Cleaned.csv
│
├── LuxuryHousing_db          # SQL Server database project/data artifact
├── backround1.jpg             # Project/dashboard visual asset
├── README.md
└── README_backup_2026-09-05.md # Original README backup
```

---

## ▶️ How to Run the Python Pipeline

### Step 1 – Install dependencies

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy pyodbc
```

### Step 2 – Run data cleaning

```bash
python Main/data_cleaning.py
```

This generates the cleaned dataset:

```text
dataset/Luxury_Housing_Cleaned.csv
```

### Step 3 – Run EDA

```bash
python Main/eda_analysis.py
```

### Step 4 – Load data into SQL Server

Configure your SQL Server connection in `Main/load_to_sql.py`, then run:

```bash
python Main/load_to_sql.py
```

### Step 5 – Build/refresh the Power BI analysis

Connect Power BI to the SQL Server analytical data and use the project dimensions and measures to explore market, builder, pricing and configuration performance.

---

## ⚠️ Reproducibility Note

The Python scripts currently contain local Windows file paths and a database connection configuration. These values should be changed to match the local environment before running the project.

For production-quality implementation, database credentials should be stored in environment variables or a secure configuration file rather than directly inside source code.

---

## 🚀 Future Improvements

Potential next steps for this project include:

- Add a dedicated SQL query layer for reusable business KPIs
- Add advanced SQL analysis using CTEs and window functions where appropriate
- Add automated data-validation checks
- Add a documented Power BI dashboard preview
- Add KPI definitions and business formulas
- Automate the ETL pipeline
- Add data-quality and anomaly checks
- Improve deployment and environment configuration

---

## 📌 Conclusion

**Luxury Housing Sales Analysis – Bengaluru** demonstrates how a Data Analyst can transform a large raw dataset into a structured analytical solution using **Python, SQL Server and Power BI**.

The project covers the complete analytics lifecycle:

**Data Preparation → EDA → Database Integration → Business Analysis → Dashboarding → Insights**

It is intended to showcase practical **Data Analyst skills, business thinking, data visualization and end-to-end analytics workflow** in a recruiter-friendly portfolio project.

---

## 👤 Portfolio

**Abhishek Pal** — Data Analyst | SQL | Python | Power BI | Excel

If you find this project useful, feel free to explore the repository and the other analytics projects in my GitHub profile.