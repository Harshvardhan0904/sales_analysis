# 📊 Data Analysis Project using Azure SQL Database

## Overview
This project focuses on analyzing business data stored across multiple tables such as vendor invoices, sales, and purchases.  
Raw CSV files were uploaded into an **Azure SQL Database**, cleaned using Python, and then analyzed to extract meaningful insights.

The main objective:
- Upload structured CSV data into Azure SQL
- Clean and prepare data for analysis
- Perform analysis on multi-table business data

---

## Data Tables
The following tables were created in Azure SQL Database from CSV files:

- `vendor_invoice` – vendor billing information  
- `sales` – sales transactions  
- `sales_detail` – detailed sales line items  
- `purchase` – purchase records  
- `purchase_detail` – detailed purchase line items  

Each CSV file was mapped to a corresponding SQL table.

---

## Tech Stack
- Python  
- Pandas  
- SQLAlchemy  
- Azure SQL Database  
- ODBC Driver 18 for SQL Server  

**References:**
- Azure SQL: https://learn.microsoft.com/en-us/azure/azure-sql/  
- Pandas: https://pandas.pydata.org/docs/  
- SQLAlchemy: https://docs.sqlalchemy.org/  

---

## Project Workflow

### 1. Database Connection
A reusable function was implemented to establish a connection between Python and Azure SQL Database using SQLAlchemy and ODBC.

Purpose:
- Centralized connection handling
- Cleaner and reusable code

---

### 2. Data Ingestion
CSV files were read using Pandas and uploaded into Azure SQL tables.

Key points:
- Automated ingestion for multiple CSV files
- Tables created directly in Azure SQL
- Supports large datasets using chunking

Reference:  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html

---

### 3. Data Cleaning
A dedicated cleaning function was created to ensure high-quality data before analysis.

Cleaning steps included:
- Handling missing values
- Removing duplicate records
- Correcting data types
- Basic data validation

Reason:
Bad data leads to incorrect analysis.

Reference:  
https://pandas.pydata.org/docs/user_guide/missing_data.html

---

### 4. Data Analysis
Cleaned data was analyzed using SQL queries and Pandas operations.

Analysis examples:
- Sales vs purchase comparison
- Vendor-wise invoice analysis
- Trend analysis on sales data
- Aggregations using SQL and Pandas

Reference:  
https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql

---

## Functions Implemented
- `connecting_db()` – connects to Azure SQL Database  
- `ingesting_data()` – uploads CSV files into SQL tables  
- `data_processing()` – cleans and prepares data for analysis  

These functions improve code reusability and maintainability.

---

## Key Learnings
- Working with real-world multi-table datasets
- Integrating Python with Azure SQL Database
- Importance of data cleaning before analysis
- Writing modular and reusable code

---

## Future Enhancements
- Add SQL stored procedures
- Build dashboards using Power BI
- Add logging and exception handling
- Automate the pipeline using Azure services

---

## References
- Azure SQL Documentation: https://learn.microsoft.com/en-us/azure/azure-sql/  
- Pandas Documentation: https://pandas.pydata.org/docs/  
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/  
- SQL Queries: https://learn.microsoft.com/en-us/sql/t-sql/
