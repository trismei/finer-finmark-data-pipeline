# FinerFinmark Data Cleaning & SQL Storage

## Overview

This project automates the cleaning and storage of financial datasets for the Finmark platform. It processes raw CSV files (event logs, marketing summaries, trend reports), cleans and standardizes the data, and stores the results in a structured SQLite database (`finmark_database.db`) using SQLAlchemy.

---

## Features

- **Automated Data Cleaning:**  
  Cleans event logs, marketing summaries, and trend reports using dedicated cleaning functions.
- **Converts valid CSV files to Readable Data Array:**  
  Accepts raw CSV files as input.
- **Database Storage:**  
  Stores cleaned data in normalized tables within an SQLite database.
- **Extensible Models:**  
  Uses SQLAlchemy ORM models for easy schema management and future expansion.

---

## Usage

### 1. **Input**

- Place your raw CSV files in the appropriate directory.
- Supported file types:
  - `event_log*.csv`
  - `marketing_summary*.csv`
  - `trend_report*.csv`

### 2. **Run the Cleaning Script**


```bash
python clean_code_automation\clean_data_main.py clean_code_automoation\datasets\{filename}
```

If running the code elsewhere
```
  set PYTHONPATH=E:\MMDC\S3101-PlatformTechnologies_FinerFinmark
  python clean_code_automation\clean_data_main.py clean_code_automation\datasets\yourfile.csv
```

- The script will automatically detect the file type and apply the correct cleaning function.

### 3. **Output**

- Cleaned data is written directly to the SQLite database in the Main Folder:  
  `S3101-PlatformTechnologies_FinerFinmark\finmark_database.db`

---

## Database Structure

The database contains the following tables:

### `event_logs`
| Column      | Type      | Description                |
|-------------|-----------|----------------------------|
| event_id    | Integer   | Primary key, autoincrement |
| user_id     | String    | User identifier            |
| event_type  | String    | Type of event              |
| product_id  | String    | Product involved           |
| amount      | Numeric   | Transaction amount (2 decimals) |
| date        | Date      | Event date                 |
| time        | Time      | Event time                 |

### `marketing_summary`
| Column        | Type      | Description                |
|---------------|-----------|----------------------------|
| event_id      | Integer   | Primary key, autoincrement |
| date          | Date      | Summary date               |
| users_active  | Integer   | Number of active users     |
| total_sales   | Numeric   | Total sales (2 decimals)   |
| new_customers | Integer   | New customers count        |
| report_date   | Date      | Date of report generation  |
| report_time   | Time      | Time of report generation  |
| percent_customer_change_per_day(%)   | float      | Shows the change in customer number per from the previous day. Negative (-) indicates a net loss in customer from previous day, Positive values indicates a net gain from previous day  |
| sales_growth_rate   | Float      | Shows the change in net sales per from the previous day. Negative (-) indicates a net loss in amount sales from previous day, Positive values indicates a net gain from previous day  |
| percent_customer_change_per_day(%)   | float      | Shows the change in customer number per from the previous day. Negative (-) indicates a net loss in customer from previous day, Positive values indicates a net gain from previous day  |
| avg_sales_per_user(P)   | Float      | Shows how much on average each customer spends within the site per day  |



### `trend_report`
| Column        | Type      | Description                |
|---------------|-----------|----------------------------|
| event_id      | Integer   | Primary Key, autoincrement |
| week_start    | Date      | Start of Week              |
| week_end      | Date      | End of Week                |
| avg_users     | Integer   | Average Users for the week |
| sales_growth_rate| Numeric| Weekly Growth Rate         |

---

## Example

**Input:**  
A file named `event_logs.csv` or `marketing_summary.csv` or `trend_report.csv` containing raw data log data.

**Output:**  
Cleaned records are inserted into the `event_logs` table in `finmark_database.db`.  
Each record receives a unique, autoincremented `event_id`.

---

## Error Handling

If the code detects that one or more of the columns are missing. An error will be displayed

## Requirements

- Python 3.8+
- pandas
- SQLAlchemy
- numpy
- Flask (Initiate Database)
- pandera (Schema Validation)

Install dependencies:
```bash
pip install pandas sqlalchemy, pandas, numpy, flask
```

---

## Extending

- To add new data types or tables, define new models in `models.py` and update the cleaning logic in `clean_data_main.py`.

---

## License

MIT License

---