# RiskLens

> ⚠️ **Work in Progress** — Project structure is set up. Code implementation is actively in progress.

**ML-powered credit risk scoring with explainable AI**

An end-to-end machine learning pipeline built in Python to predict credit default risk using the German Credit dataset. The system will automate data ingestion, preprocessing, model training, and scoring, with SHAP-based explainability to make predictions interpretable.

---

## Features (Planned)

- **End-to-End ML Pipeline** --> Raw data ingestion through scored predictions with no manual handoffs
- **Credit Risk Classification** --> Predict likelihood of loan default across 1,000 borrower records using 17 features
- **Automated Preprocessing** --> Encode categorical variables, scale features, and split train/test sets
- **Model Training** --> Random Forest classifier via `scikit-learn` with accuracy and ROC-AUC evaluation
- **Explainable AI (XAI)** --> SHAP-based feature importance to surface which factors drive each prediction
- **SQL Schema** --> SQLite schema for structured storage and querying of raw and scored credit records

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.10+ |
| ML | scikit-learn |
| Data Processing | Pandas, SQL |
| Explainability | SHAP |
| Database | SQLite / SQLAlchemy |

---

## Project Structure

```
RiskLens/
│
├── data/
│   └── raw/
│       └── credit.csv          # German Credit dataset (1,000 records)
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py        # Data loading, encoding, scaling
│   ├── features.py             # Feature selection & engineering
│   ├── model.py                # Model training & evaluation
│   └── predict.py              # Scoring & inference
│
├── models/                     # Saved model output (auto-generated on run)
│
├── sql/
│   └── schema.sql              # SQLite schema for credit risk records
│
├── main.py                     # Runs the full pipeline end-to-end
├── requirements.txt
└── README.md
```

---

## Pipeline Overview (Planned)

```
Raw Data (credit.csv)
        │
        ▼
Preprocessing (preprocessing.py)
        │  • Encode categorical columns
        │  • Scale numeric features
        │  • Train/test split
        ▼
Feature Engineering (features.py)
        │  • Feature selection
        │  • Derived risk indicators
        ▼
Model Training (model.py)
        │  • Random Forest classifier
        │  • Accuracy + ROC-AUC evaluation
        ▼
Risk Score Output (predict.py)
        │  • Per-record default probability
        │  • Exported predictions
        ▼
Explainability
           • SHAP feature importance
           • Risk factor breakdown
```

---

## Dataset

Uses the [German Credit Dataset](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) — a widely used benchmark in credit risk ML.

- **1,000 records**, 17 features
- **Target:** `default` (yes/no)
- **Class split:** 70% no default, 30% default
- **Zero null values**

Key features include `checking_balance`, `credit_history`, `months_loan_duration`, `savings_balance`, `employment_duration`, `age`, and `existing_loans_count`.

---

## Roadmap

- [ ] Implement preprocessing pipeline
- [ ] Implement feature engineering
- [ ] Train and evaluate Random Forest model
- [ ] Build prediction & scoring module
- [ ] Complete SHAP explainability module
- [ ] Add EDA notebook
- [ ] Build interactive dashboard (Streamlit or Power BI)

---

## Getting Started

> ⚠️ Pipeline not yet runnable: implementation in progress.

```bash
# Clone the repository
git clone https://github.com/Sarim78/RiskLens.git
cd RiskLens

# Install dependencies
pip install -r requirements.txt

# Run the pipeline (once implemented)
python main.py
```
