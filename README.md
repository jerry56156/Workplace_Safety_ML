# Early-Warning System for Workplace Safety  
**Machine Learning Proof of Concept (PoC)**

## Overview
This repository contains a **proof of concept (PoC)** for an **early-warning system** that uses historical OSHA injury and exposure data to identify workplaces that may be at elevated safety risk.

The goal is **not** to perfectly predict workplace incidents. Instead, this project demonstrates a defensible data pipeline, correct handling of OSHA Form 300A metrics, and a realistic machine-learning framing for occupational safety analytics.

---

## Core Idea
Risk is defined **relative to industry peers**, not by a single global threshold.

An establishment is labeled **high risk** if its incident rate is **above the median incident rate for its NAICS industry**. This avoids unfairly penalizing inherently higher-risk industries (e.g., mining) and aligns with how safety performance is typically evaluated.

---

## Data Sources
- **OSHA Establishment-Specific Injury and Illness Data (Form 300A)**  
  https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data

- **Nutrien Rocanville Potash Mine** (contextual reference only)  
  https://www.cim.org/past-award-winners/nutrien-rocanville-mine/

All injury definitions and formulas follow OSHA standards.

---

## Repository Structure
.
├── filter_script.py
├── filtered2016.csv
├── filtered2017.csv
├── filtered2018.csv
├── filtered2019.csv
├── filtered2020.csv
├── filtered2021.csv
├── filtered2022.csv
├── filtered2023.csv
├── filtered2024.csv
├── nutrien.csv
├── OSHA_Safety_Incident_ML.ipynb
└── README.md

---

## Methodology

### Data Processing
- Yearly OSHA datasets are loaded and combined
- NAICS codes are treated as categorical identifiers
- Invalid exposure rows (zero or missing hours/employees) are removed
- Columns are renamed to reflect OSHA semantics:
  - `reported_avg_employees`
  - `reported_total_hours`

### OSHA Metrics
**Total Recordable Cases (TRC):**
TRC = DAFW + DJTR + Other Recordable Cases

---

## Risk Labeling
- Incident rates are compared **within NAICS industries**
- Labels are assigned as:
  - `1` → Above industry median (higher risk)
  - `0` → At or below industry median (lower risk)

This produces balanced, interpretable labels for early-warning analysis.

---

## Model
- **Gradient Boosting Classifier**
- Features:
  - NAICS code (one-hot encoded)
  - Reported average employees
  - Reported total hours worked

A lower probability threshold is used to prioritize **recall**, reflecting safety contexts where missing risk is more costly than false alarms.

---

## Evaluation
The following metrics are reported:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve and AUC

Moderate accuracy (~0.55–0.65) is expected due to noisy real-world safety data, limited feature scope, and peer-relative labeling.

---

## Scenario Simulation
A hypothetical **potash mining facility** is evaluated under:
- baseline conditions,
- increased workforce size,
- increased total hours worked.

This demonstrates how the model could support **what-if safety planning**, not operational decision-making.

---

## Key Takeaways
- Risk should be evaluated **relative to industry peers**
- OSHA injury data is inherently noisy and stochastic
- Exposure validation is critical to avoid corrupted rates
- Accuracy is not the primary success metric for early-warning systems
- Simple size-based features have limited predictive power
- This PoC demonstrates methodology, not deployment readiness

---

## Limitations
This is a **proof of concept**, not a production system.

Not included:
- time-lagged incident history,
- near-miss data,
- inspections, audits, or training records,
- contractor vs employee separation,
- overtime, shift, or seasonal effects.

Results should be interpreted directionally only.

---

## Intended Use
- Technical interviews
- Safety analytics demonstrations
- Early-stage modeling discussions

**Not intended for deployment or regulatory decision-making.**

---

## Disclaimer
This project is for **educational and exploratory purposes only**.  
All outputs are illustrative and should not be used for operational, legal, or compliance decisions.
