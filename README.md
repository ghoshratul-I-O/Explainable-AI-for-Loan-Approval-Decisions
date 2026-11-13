# Explainable AI - Loan Default Prediction

An end-to-end Machine Learning project to predict vehicle loan defaults with explainability (SHAP) and deployment-ready architecture.

## Project Structure

```text
Loan/
├── data/                      # Dataset files (train.csv, test.csv, sample_submission.csv)
├── notebooks/                 # Jupyter notebooks for iterative, phased analysis
│   └── 01_EDA.ipynb           # Phase 1: Exploratory Data Analysis & data understanding
├── models/                    # Serialized models and scalers (future phase)
├── reports/                   # Generated reports and figures
│   └── visualizations/
├── app.py                     # Streamlit application (future phase)
├── requirements.txt           # Project dependencies
├── .gitignore                 # Ignored files (data files, cache, virtual environment)
├── GEMINI.md                  # Project rules & phase tracking
└── README.md                  # Project overview and roadmap
```

## Workflow Constraints & Rules
- **Phase-by-phase execution:** Code is developed interactively per phase.
- **Strict Leakage Prevention:** `data/test.csv` is never inspected or evaluated during EDA, feature engineering, or training.
- **Explainability Focus:** Clear feature importance and decision explanations suitable for production and engineering discussions.

## Current Status
- **Active Phase:** Phase 1 — Dataset Understanding and Exploratory Data Analysis.
- **Next Step:** Run initial cells in `notebooks/01_EDA.ipynb` to inspect dimensions, data types, and initial records of `data/train.csv`.

