<div align="center">
  
# Machine Learning Risk Scoring System

**End-to-end ML pipeline for credit & operational risk prediction**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

</div>

---

## Overview

A full end-to-end machine learning pipeline built in Python to predict **credit risk** and **operational risk scores** across financial datasets. The system automates data ingestion, preprocessing, model training, and evaluation, with results surfaced through an explainable Power BI dashboard that makes predictions interpretable for non-technical stakeholders.

---

## Features

- **End-to-End ML Pipeline** — Covers raw data ingestion through model output, with no manual handoffs between stages
- **Dual Risk Scoring** — Predicts both credit risk and operational risk, enabling multi-dimensional financial analysis
- **Automated Preprocessing & Validation** — SQL + Pandas routines enforce schema validation, outlier handling, and feature engineering, improving data reliability by **25%**
- **Model Training** — Implements classification and regression models using `scikit-learn` and `TensorFlow`
- **Explainable AI (XAI)** — Integrates interpretability components so decision-makers can understand model outputs
- **Power BI Dashboard** — Interactive visualizations of risk scores, model confidence, and feature importance

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.10+ |
| ML Frameworks | scikit-learn, TensorFlow |
| Data Processing | Pandas, SQL |
| Visualization | Power BI |
| Explainability | SHAP / feature importance |

---

## Project Structure

```
Machine-Learning-Risk-Scoring-System/
│
├── data/
│   ├── raw/                  # Raw input datasets
│   └── processed/            # Cleaned, validated data
│
├── notebooks/
│   ├── eda.ipynb             # Exploratory data analysis
│   └── model_experiments.ipynb
│
├── src/
│   ├── preprocessing.py      # SQL + Pandas data pipeline
│   ├── features.py           # Feature engineering
│   ├── model.py              # Model training & evaluation
│   └── predict.py            # Scoring & inference
│
├── dashboard/
│   └── risk_dashboard.pbix   # Power BI dashboard file
│
├── requirements.txt
└── README.md
```

---

## Pipeline Overview

```
Raw Data (SQL)
     │
     ▼
Preprocessing & Validation (Pandas)
     │  • Schema checks
     │  • Outlier removal
     │  • Feature engineering
     ▼
Model Training
     │  • scikit-learn (Logistic Regression, Random Forest, XGBoost)
     │  • TensorFlow (Neural network risk scorer)
     ▼
Risk Score Output
     │  • Credit Risk Score
     │  • Operational Risk Score
     ▼
Power BI Dashboard
     │  • Predictions visualization
     └  • Explainable AI components (SHAP values, feature importance)
```

---

## Results

| Metric | Value |
|---|---|
| Data reliability improvement | +25% |
| Risk types modeled | Credit & Operational |
| Dashboard components | Explainable AI-enhanced |
| Pipeline automation | Fully automated (end-to-end) |

---

## Getting Started

### Prerequisites

```bash
Python 3.10+
pip install -r requirements.txt
```

### Installation

```bash
# Clone the repository
git clone https://github.com/Sarim78/Machine-Learning-Risk-Scoring-System.git
cd Machine-Learning-Risk-Scoring-System

# Install dependencies
pip install -r requirements.txt
```

### Run the Pipeline

```bash
# Preprocess data
python src/preprocessing.py

# Train the model
python src/model.py

# Generate risk scores
python src/predict.py
```

---

## Dashboard

Risk predictions are visualized in a Power BI dashboard (`dashboard/risk_dashboard.pbix`) featuring:

- Credit and operational risk score distributions
- Per-record prediction confidence
- Feature importance charts (XAI)
- Trend analysis over time
