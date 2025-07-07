# Finer FinMark: Scalable Data Pipeline

This repository contains the full analytics pipeline and data cleaning solution for **Project Finer FinMark** — a major system upgrade initiative to help FinMark Corporation scale from **500 to 3,000+ daily orders**. The project addresses performance bottlenecks, missing real-time insights, and the need for privacy-compliant data systems.

---

## Objectives
- ✅ Build a scalable, hybrid data pipeline using batch (Airflow) and real-time (Kafka) ingestion
- ✅ Clean and structure three core datasets: event logs, marketing summaries, and weekly trend reports
- ✅ Enable fast, accurate dashboards for Marketing, Product, Ops, and Finance teams
- ✅ Align with PDPA/GDPR regulations through privacy-first architecture
- ✅ Support predictive forecasting to anticipate order surges, restocking needs, and user growth

---
## Quick Start

### Clone the Repository
```bash
git clone <repo-url>
cd finer-finmark-data-pipeline
```

### macOS / Linux
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)
```powershell
py -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

Raw CSV files belong in `clean_code_automation/datasets`. Run the cleaner:
```bash
python clean_code_automation/clean_data_main.py datasets/<your_file.csv>
```
Cleaned data is written to `finmark_database.db`.

For troubleshooting tips see
[`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md). A detailed
progress log is available in
[`docs/PROJECT_NOTES.md`](docs/PROJECT_NOTES.md).

---
## Folder Structure 
```bash
finer-finmark-data-pipeline/
├── clean_code_automation/               # data cleaning package
│   ├── README.md                        # overview and usage of the cleaner
│   ├── clean_data_main.py               # entry point to run the cleaner
│   ├── datasets/                        # raw CSV inputs
│   │   ├── event_logs.csv
│   │   ├── marketing_summary.csv
│   │   ├── trend_report.csv
│   │   └── cleaned/                     # timestamped outputs
│   └── functions/                       # cleaning helpers
│       ├── clean_event_logs.py
│       ├── clean_marketing_summary.py
│       ├── clean_trend_report.py
│       └── schema_validation.py
├── sql-data-storage/                    # database utilities
│   ├── README.md
│   └── src/
│       ├── main.py
│       ├── db/
│       │   ├── connection.py
│       │   ├── initialize_db.py
│       │   ├── models.py
│       │   └── utils.py
│       └── ingest/
│           └── load_data.py
├── docs/                                # project notes and troubleshooting
│   ├── PROJECT_NOTES.md
│   └── TROUBLESHOOTING.md
├── cleaned_event_logs.ipynb             # notebook examples
├── cleaned_marketing_summary.ipynb
├── cleaned_trend_report.ipynb
├── event_logs.csv                       # sample raw data
├── marketing_summary.csv
├── trend_report.csv
├── final_cleaned_event_logs.csv         # sample cleaned outputs
├── final_cleaned_marketing_summary.csv
├── final_cleaned_trend_report.csv
├── requirements.txt
└── README.md
```

---

## Datasets

| Dataset                  | Description                                           |
|--------------------------|-------------------------------------------------------|
| `event_logs.csv`         | User interaction and purchase events (raw logs)       |
| `marketing_summary.csv`  | Weekly performance metrics from marketing campaigns   |
| `trend_report.csv`       | Time-based patterns for forecasting and strategy      |

Each dataset has a corresponding `.ipynb` cleaning file with:
- Null/missing value treatment
- Outlier capping (IQR method)
- Column renaming based on verified reports
- Final `.csv` output for modeling or dashboarding

---

## Dashboard Panels

Final mockups follow a unified dark-mode UI and are divided into 4 functional panels:

1. **Real-Time Order Operations**  
   → Ops & CTO visibility into platform load, order latency, system health

2. **User Journey & Feature Usage**  
   → Product team dashboard showing drop-offs, feature engagement, A/B results

3. **Conversion & Campaign Insights**  
   → Marketing KPIs: CTR, ROAS, conversion by source & region

4. **Forecast & Planning**  
   → Finance & Growth team forecast of order volume, inventory alerts, return rate trends

See all mockups in `/visuals`.

---

## Data Privacy & Compliance

- ✅ Hashed user IDs
- ✅ Consent-based event tracking
- ✅ PDPA/GDPR-aligned export/delete functionality
- ✅ Role-based access model for data views

---

## Tech Stack

| Layer          | Tools/Frameworks                     |
|----------------|--------------------------------------|
| Ingestion      | Apache Kafka, Apache Airflow         |
| Processing     | dbt, Python (Prophet/ARIMA), Pandas  |
| Storage        | Snowflake, BigQuery, S3, GCS         |
| Dashboards     | Power BI, Tableau                    |
| Monitoring     | Prometheus + Grafana                 |
| Notifications  | Slack (Webhooks/Bot)         |

---

## Business Impact

| Insight Category       | Example Questions Answered                                |
|------------------------|------------------------------------------------------------|
| Product Scaling        | What features are being ignored? What modules cause churn? |
| Customer Experience    | Where do users drop off? Which screens cause friction?     |
| Business Planning      | When will orders surge? When should we restock?            |
| Campaign Performance   | Which channel brings highest ROAS? Where to cut spend?     |

---

## Author

**Tris Atienza, Anthony Quitay, Lizette Dejucos, Marievic Reyes, Franchella Martini Micu-Paculan**  
Data Analyst | System Architect | Strategy Consultant  
📍 MMDC | 🎓 BSIT Major in Data Analytics

For a detailed setup guide and project progress notes, see
[`docs/PROJECT_NOTES.md`](docs/PROJECT_NOTES.md).

---



