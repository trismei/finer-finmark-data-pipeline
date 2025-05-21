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

## Folder Structure 
<pre> ``` finer-finmark-data-pipeline/ ├── data/ │ ├── raw/ # Original files (event_logs.csv, etc.) │ ├── cleaned/ # Cleaned datasets (final_cleaned_*.csv) │ └── reports/ # PDF reports used as references │ ├── notebooks/ # Jupyter notebooks for cleaning + EDA │ ├── cleaned_event_logs.ipynb │ ├── cleaned_marketing_summary.ipynb │ └── cleaned_trend_report.ipynb │ ├── visuals/ # All images, diagrams, dashboards │ ├── current_pipeline.png │ ├── proposed_pipeline.png │ ├── FinMark_Control_Hub.png │ ├── Real-Time_Order_Operations.png │ ├── User_Journey_Feature_Usage.png │ ├── Conversion_Campaign_Insights.png │ └── Forecast_Planning.png │ ├── pipeline/ # (Optional) Scripts for ETL / Airflow / Alerts │ ├── airflow_dag_sample.py │ ├── slack_alert_template.py │ └── dbt_models/ │ ├── dashboard_specs/ # Layouts, widget descriptions, KPIs │ ├── control_hub_overview.md │ └── panel_breakdowns.md │ ├── README.md # Final documentation ├── .gitignore # Ignore .ipynb_checkpoints, etc. └── requirements.txt # Environment packages ``` </pre>


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


---



