# Early-Warning System for Workplace Safety  
**Machine Learning Proof of Concept (PoC)**

## Overview
This repository contains a **proof of concept (PoC)** for an **early-warning system** that uses historical OSHA injury and exposure data to identify workplaces that may be at elevated safety risk.

The objective is **not** to perfectly predict accidents, but to demonstrate a defensible, transparent approach to:
- handling OSHA 300A data correctly,
- defining risk in a meaningful way,
- building and evaluating a baseline ML model for safety analytics.

This project is intentionally scoped and simplified for clarity and explainability.

---

## Key Concept
Risk is defined **relative to industry peers**, not by a single global threshold.

An establishment is considered *high risk* if its incident rate is **higher than the median incident rate for the same NAICS industry**.  
This avoids unfairly labeling inherently high-risk industries (e.g., mining) as unsafe simply due to their nature.

---

## Data Sources
- **OSHA Establishment-Specific Injury and Illness Data (Form 300A)**  
  https://www.osha.gov/Establishment-Specific-Injury-and-Illness-Data

- **Nutrien Rocanville Potash Mine** (contextual reference only)  
  https://www.cim.org/past-award-winners/nutrien-rocanville-mine/

All definitions and formulas follow OSHA standards.

---

## Repository Structure
