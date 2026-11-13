# Explainable AI for Loan Default Prediction

An end-to-end Machine Learning project to predict vehicle loan default risk and interpret predictions using Explainable AI (SHAP, LIME), fairness auditing, and an interactive Streamlit application.

**Dataset:** LTFS Vehicle Loan Default Prediction (India)  
**Objective:** Predict the likelihood of loan default and explain the primary drivers behind each individual decision.

---

## Development Roadmap

| Phase | Task | Key Techniques & Tools |
| :--- | :--- | :--- |
| **Phase 1** | **Dataset Understanding & EDA** | Pandas, Matplotlib, Seaborn |
| **Phase 2** | **Data Cleaning & Preprocessing** | Outlier handling, encoding, missing imputation |
| **Phase 3** | **Feature Engineering** | Date parsing, tenure durations, ratio features |
| **Phase 4** | **Model Training & Comparison** | Logistic Regression, Decision Tree, Random Forest, XGBoost |
| **Phase 5** | **Model Evaluation** | Precision, Recall, F1, ROC-AUC, PR-AUC, Threshold optimization |
| **Phase 6** | **Explainable AI (XAI)** | SHAP (Global & Local values), LIME |
| **Phase 7** | **Fairness & Bias Analysis** | Fairlearn (demographic parity, equalized odds) |
| **Phase 8** | **Dashboard Development** | Streamlit (Risk overview, prediction engine, what-if simulator) |
| **Phase 9** | **Deployment & Documentation** | Streamlit Community Cloud, GitHub |

---

## Application Features
1. **Portfolio Risk Dashboard:** High-level default statistics, risk segments, and portfolio health.
2. **Real-time Default Predictor:** Enter applicant details to get instant risk probability.
3. **Explainable AI (XAI):** Waterfall and force plots visualizing why an applicant was approved or flagged.
4. **Interactive "What-If" Simulator:** Tweak parameters (loan amount, down payment, bureau score) to observe impact on risk.

---

## Project Structure

```text
Loan/
├── data/
│   ├── train.csv                      # Training data (233,154 records)
│   ├── test.csv                       # Test data (held-out)
│   ├── sample_submission.csv
│   └── data_dictionary.md             # Comprehensive schema reference
├── notebooks/
│   └── EDA.ipynb                      # Phase 1: Interactive EDA & hypothesis testing
├── models/                            # Trained pipelines & serialized models
├── reports/
│   └── visualizations/                # Generated publication-quality figures
├── app.py                             # Streamlit web application
├── requirements.txt                   # Environment dependencies
├── .gitignore                         # Data & environment exclusion rules
├── GEMINI.md                          # Workflow rules & active phase tracker
└── README.md                          # Project documentation & roadmap
```

---

## Current Status
- **Active Phase:** **Phase 1 — Dataset Understanding and Exploratory Data Analysis (`notebooks/EDA.ipynb`)**
- **Next Step:** Run univariate and bivariate analysis on credit attributes, loan-to-value (LTV), and bureau scores.
