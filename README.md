<<<<<<< HEAD
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
=======
Autonomous Fleet Telemetry & Predictive Maintenance HubAn end-to-end telemetry monitoring and predictive maintenance analytics dashboard built on the NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) turbofan engine dataset.This platform processes streaming operational sensor metrics to calculate Remaining Useful Life (RUL) and detect multivariate time-series anomalies, enabling proactive maintenance scheduling and reducing catastrophic fleet failures.ðŸŽ¯ Executive Summary & Business ImpactProblem Statement: Unscheduled maintenance and unexpected equipment failure in fleet assets result in severe downtime costs and logistical bottlenecks. Traditional threshold alerts often fire too late or produce high false-positive rates.Solution: Implemented a dynamic telemetry pipeline using rolling statistical baselines and dynamic Z-score thresholds to flag sensor degradation profiles prior to critical system failure.Key Metrics & Outcomes:30-Cycle Early Warning Window: Categorizes asset health into CRITICAL, WARNING, and HEALTHY states based on degradation trajectories.Automated Anomaly Detection: Flags sensor drift exceeding $\pm 2.5\sigma$ from historical baseline averages.Interactive Decision Support: Serves real-time telemetry metrics via a high-performance interactive Streamlit application.ðŸ› ï¸ System Architecture & Methodology+--------------------------+       +---------------------------+       +------------------------------+
| NASA C-MAPSS Sensor Data |  -->  | Feature Engineering &     |  -->  | Interactive Executive        |
| (21 Telemetry Channels)  |       | Rolling Z-Score Analytics |       | Streamlit Dashboard          |
+--------------------------+       +---------------------------+       +------------------------------+
Telemetry Processing Pipeline:Parsed high-frequency time-series datasets representing multi-sensor engine operational cycles.Derived exact Remaining Useful Life (RUL) per asset by identifying engine end-of-life (EOL) cycles.Statistical Anomaly Engine:Computed 10-cycle rolling averages across sensitive temperature metrics (sensor_11).Transformed raw signals into normalized Z-scores ($Z = \frac{X - \mu}{\sigma}$) to detect sudden degradation anomalies while filtering high-frequency operational noise.Interactive UI / UX:Built responsive dashboard architecture using Streamlit, featuring executive KPI cards, fleet filtering sidebars, and dual-axis signal visualization charts.ðŸš€ Key FeaturesReal-time KPI Metrics: Instant visibility into Current Cycle, RUL, Health Status, and Cumulative Anomaly Counts.Fleet Asset Selection: Seamlessly pivot across 100+ simulated engine units to inspect individual health trajectories.Signal Degradation Profile: Visual representation comparing smoothed sensor averages against Z-score anomaly bounds.ðŸ’» Tech StackLanguage: Python 3.11+Dashboarding & UI: StreamlitData Processing: Pandas, NumPyStatistical Modeling: SciPy, StatsmodelsData Visualization: Matplotlib, SeabornðŸ“¦ Quick Start & SetupPrerequisitesPython 3.10 or higherGitInstallationClone the repository:git clone https://github.com/YOUR_USERNAME/fleet-analytics-dashboard.git
cd fleet-analytics-dashboard
Install dependencies:pip install pandas numpy scipy matplotlib seaborn streamlit
Run the Streamlit application:python -m streamlit run app.py
Open your browser at http://localhost:8501.ðŸ“‚ Project Structurefleet-analytics-dashboard/
â”œâ”€â”€ app.py                # Main Streamlit dashboard script
â”œâ”€â”€ train_FD001.txt       # NASA C-MAPSS Turbofan Engine degradation dataset
â”œâ”€â”€ README.md             # Technical documentation & project brief
âœ‰ï¸ Author & ContactDeveloper: Arunava BiswasFocus: Data Analytics, Machine Learning Engineering, & Predictive MaintenanceLinkedIn: Connect on LinkedInGitHub: GitHub Profile
>>>>>>> cd39c69e181a0facfdf7ef95fb1d12f92cf09637
