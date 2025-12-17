# Luxury Housing Sales Analysis – Bengaluru

## Project Overview
This project is an end-to-end **Real Estate Data Analytics solution** focused on analyzing **luxury housing sales in Bengaluru**.  
It demonstrates a real-world **data pipeline** using **Python for data cleaning & EDA**, **SQL Server for data warehousing**, and **Power BI for interactive dashboarding**.

The project works on a large dataset (100,000+ records) and is designed to replicate an **enterprise-level analytics workflow**.

---

## Problem Statement
Build a complete real estate analytics solution using Python for advanced data cleaning, load the refined dataset into a SQL database, and connect Power BI directly to SQL to build an interactive dashboard.  
The goal is to generate **actionable business insights** for real estate stakeholders.

---

## Business Use Cases Covered
- **Market Intelligence**  
  Identify high-performing micro-markets and locality-wise trends.
- **Builder Performance Analysis**  
  Compare builders based on total revenue and average ticket price.
- **Competitive Pricing**  
  Analyze pricing strategies across configurations and builders.
- **Buyer Persona Analysis**  
  Understand buyer behavior using Buyer Type and Buyer Comments.
- **Amenity Impact on Conversion**  
  Analyze the relationship between average amenity score and booking conversion rate.
- **Quarterly Trend Tracking**  
  Track booking patterns across fiscal quarters.
- **Configuration Demand**  
  Identify the most in-demand configurations (3BHK, 4BHK, 5BHK+).

---

## Tech Stack
- **Python**: Pandas, NumPy (Data Cleaning & EDA)
- **SQL Server**: Data Warehousing & Querying
- **Power BI**: Dashboarding & Data Visualization
- **SQLAlchemy & PyODBC**: Python–SQL integration
- **Git & GitHub**: Version control

---

## Dataset Details
- **Size**: 100,000+ rows  
- **Key Columns**:
  - Property_ID
  - Micro_Market
  - Project_Name
  - Developer_Name
  - Unit_Size_Sqft
  - Configuration
  - Ticket_Price_Cr
  - Transaction_Type
  - Buyer_Type
  - Purchase_Quarter
  - Amenity_Score
  - Connectivity_Score
  - Possession_Status
  - Sales_Channel
  - NRI_Buyer
  - Buyer_Comments

---

## Project Workflow

### Python – Data Cleaning & EDA
- Loaded raw CSV dataset
- Cleaned currency fields (₹, Cr, encoding issues)
- Handled missing values:
  - Amenity_Score → filled using average
  - Buyer_Comments → handled to avoid nulls
- Removed duplicates
- Fixed data types (dates, numerics)
- Performed EDA:
  - Distribution analysis
  - Correlation analysis
  - Outlier understanding

**Output:** Cleaned dataset ready for SQL insertion

---

### SQL – Data Warehousing
- Designed and created SQL Server table schema
- Inserted cleaned data using Python (SQLAlchemy)
- Validated data using SQL queries:
  - Total record count
  - Aggregations by builder and quarter

**Result:** Centralized, normalized SQL table with 100,000+ records

---

### Power BI – Dashboard & Insights
- Connected Power BI directly to SQL Server (Live connection)
- Built interactive dashboard with slicers:
  - Builder
  - Micro Market
  - Configuration
  - Purchase Quarter
  - Possession Status
  - Buyer Type

#### Key Visuals:
- KPI Cards:
  - Total Properties
  - Total Revenue (Cr)
  - Average Ticket Price (Cr)
  - Average Amenity Score
- Line Chart: Quarterly booking trend
- Bar Chart: Builder-wise revenue
- Donut Chart: Configuration demand
- Scatter Plot: **Average Amenity Score vs Booking Conversion %**
- Filters and cross-interactions enabled

---

## Key Insights Generated
- Certain micro-markets consistently outperform others in booking volume
- Builders with higher **average amenity scores** show better booking conversion
- 3BHK and 4BHK configurations dominate luxury housing demand
- Booking activity peaks in specific quarters, indicating seasonal trends
- NRI and HNI buyers contribute significantly to high-ticket transactions

---

## Project Evaluation Mapping
Python Data Cleaning | Complete |
SQL Integration | Complete |
Power BI Dashboard | Complete |
Business Insights | Generated |
Documentation | Complete |

---

## Conclusion
This project successfully demonstrates a **full-stack data analytics workflow** from raw data ingestion to business-ready insights.  
It closely mirrors how analytics projects are executed in real-world enterprise environments and provides meaningful insights for real estate decision-making.


