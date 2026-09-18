# Autonomous Fleet Telemetry & Predictive Maintenance Hub

An end-to-end telemetry monitoring and predictive maintenance analytics dashboard built on the NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) turbofan engine dataset.

This platform ingests streaming operational sensor metrics to compute real-time Remaining Useful Life (RUL) trajectories and detect multivariate time-series anomalies, providing early warnings before critical component degradation.

---

## ?? Executive Summary & Business Impact

* **Problem Statement:** Unscheduled maintenance and unexpected equipment failures in heavy autonomous fleets lead to exponential downtime costs, logistical delays, and severe safety risks. Traditional fixed-threshold alerts often fire too late or trigger frequent false alarms.
* **Solution:** Developed a dynamic time-series analytical engine using 10-cycle rolling baselines and adaptive statistical Z-score thresholds to detect sensor drift and degradation profiles early in an asset's life cycle.
* **Key Business Outcomes:**
  * **30-Cycle Early Warning Window:** Categorizes asset health dynamically into CRITICAL, WARNING, and HEALTHY operational states based on RUL degradation curves.
  * **Automated Anomaly Detection:** Identifies statistical temperature anomalies exceeding ±2.5s from historical baseline averages.
  * **Executive Decision Support:** Serves real-time telemetry metrics via an interactive, web-based Streamlit dashboard.

---

## ??? System Architecture & Data Pipeline

+--------------------------------+     +--------------------------------+     +--------------------------------+
¦      NASA C-MAPSS Dataset      ¦ --> ¦   ETL & Feature Engineering    ¦ --> ¦  Statistical Anomaly Engine   ¦
¦  (21 Telemetry Sensor Channels)¦     ¦  (RUL Calculation & Rolling)   ¦     ¦ (Z-Score Thresholding ±2.5s)   ¦
+--------------------------------+     +--------------------------------+     +--------------------------------+
¦
?
+--------------------------------+
¦      Interactive Dashboard     ¦
¦  (Streamlit KPI & Line Charts) ¦
+--------------------------------+


### Telemetry Pipeline:
1. **Data Ingestion:** Parsed high-frequency time-series records representing multi-sensor engine operational cycles (`train_FD001.txt`).
2. **Target Feature Engineering:** Engineered target Remaining Useful Life (RUL) metric per engine unit by determining total operational lifespan ($RUL = Cycle_{max} - Cycle_{current}$).
3. **Statistical Anomaly Detection Engine:** Calculated 10-cycle moving averages across sensitive thermal sensors (`sensor_11`). Transformed raw signals into normalized Z-scores ($Z = \frac{X - \mu}{\sigma}$) to detect degradation trends while smoothing out operational noise.
4. **Interactive UI / UX:** Engineered responsive dashboard UI featuring high-level KPI metric cards, interactive unit selection sidebars, and dual-axis signal degradation visualizers.

---

## ?? Key Features

* **Real-Time Fleet Status KPIs:** Instant visibility into Current Cycle, RUL, Engine Health Status, and Cumulative Anomaly Counts.
* **Multi-Asset Filtering:** Interactive dropdown to pivot seamlessly across 100+ simulated jet engine units.
* **Telemetry Degradation Charts:** Visual overlay comparing smoothed sensor averages against dynamic Z-score upper/lower bounds.

---

## ?? Tech Stack & Dependencies

* **Language:** Python 3.10+
* **Dashboard & UI:** Streamlit
* **Data Processing & Analytics:** Pandas, NumPy, SciPy
* **Data Visualization:** Matplotlib, Seaborn

---

## ?? Getting Started

### Prerequisites
* Python 3.10 or higher installed
* Git installed

### Quick Start Guide

1. **Clone the repository:**
   ```powershell
   git clone [https://github.com/YOUR_USERNAME/fleet-analytics-dashboard.git](https://github.com/YOUR_USERNAME/fleet-analytics-dashboard.git)
   cd fleet-analytics-dashboard
Install required dependencies:

PowerShell
python -m pip install pandas numpy scipy matplotlib seaborn streamlit
Run the Streamlit application:

PowerShell
python -m streamlit run app.py
Open your browser at http://localhost:8501.

?? Project Structure
Plaintext
fleet-analytics-dashboard/
¦
+-- app.py              # Core Streamlit application & visualization logic
+-- train_FD001.txt     # NASA C-MAPSS Turbofan engine degradation dataset
+-- README.md           # Technical documentation & project brief
+-- requirements.txt    # Python package dependencies
?? Author & Contact
Developer: Arunava Biswas

Focus: Data Analytics | Machine Learning Engineering | Predictive Maintenance

GitHub: GitHub Profile

LinkedIn: LinkedIn Profile
