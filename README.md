# Explainable-AI-for-Loan-Approval-Decisions
End-to-end vehicle loan default prediction pipeline using XGBoost, evaluated with local and global explainability via SHAP and LIME.

##### Deployed & Running webapp link : https://xai-loan-approval-decision.streamlit.app/
##### Dataset link : https://www.kaggle.com/datasets/manovirat/ltfs-dataset


## Overview

- **Dataset:** LTFS Vehicle Loan Default Prediction (India) — 233,154 records
- **Objective:** Predict borrower default risk to reduce credit losses while providing transparent decision drivers for each applicant.
- **Champion Model:** XGBoost Classifier achieving 0.656 ROC-AUC and 64.9% Recall on held-out validation data.

---

## Workflow & Methodology

1. **Exploratory Data Analysis:** Analyzed portfolio-level default distribution (~21.7% base default rate) and identified primary risk factors: Loan-to-Value (LTV) leverage, bureau credit scores, and inquiry frequency.
2. **Preprocessing & Feature Engineering:** Handled missing employment data, parsed tenure durations and applicant age, flagged thin-file borrowers, and consolidated credit bureau rating tiers.
3. **Model Benchmarking:** Trained and compared four supervised classification algorithms (Logistic Regression, Decision Tree, Random Forest, and XGBoost) using stratified validation splits.
4. **Threshold Tuning:** Evaluated the precision-recall trade-off across decision thresholds (0.30 to 0.60) to optimize default detection vs. false alarm rates.
5. **Explainable AI (XAI):** Applied SHAP TreeExplainer for global feature rankings and local waterfall explanations, validated with LIME surrogate rules.
6. **Fairness Audit:** Evaluated demographic parity across employment categories and age brackets using Fairlearn, satisfying the Four-Fifths (80%) Rule.
7. **Web Dashboard:** Built a modular Streamlit application with a portfolio health view, risk scoring engine, SHAP decision breakdown, and a counterfactual What-If simulator.

---

## Model Benchmark Results

Evaluated on 46,631 held-out validation records (stratified 80/20 split):

| Model | ROC-AUC | Recall | Precision | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **XGBoost (Champion)** | **0.656** | **64.9%** | **29.7%** | **0.408** |
| Random Forest | 0.644 | 62.2% | 28.5% | 0.399 |
| Logistic Regression | 0.631 | 60.8% | 27.2% | 0.390 |
| Decision Tree | 0.619 | 58.4% | 26.1% | 0.390 |

---

## Project Structure

```text
├── notebooks/
│   ├── EDA.ipynb                  # Exploratory data analysis
│   ├── Preprocessing.ipynb        # Data cleaning and imputation
│   ├── Feature_Engineering.ipynb  # Feature derivation and encoding
│   ├── Model_Training.ipynb       # Model comparison and threshold tuning
│   ├── Explainable_AI.ipynb       # SHAP and LIME interpretability
│   └── Fairness_Analysis.ipynb    # Fairlearn demographic parity audit
├── models/                        # Serialized model, scaler, and metadata (.pkl, .json)
├── reports/visualizations/        # High-resolution figures (.png)
├── app.py                         # Streamlit application
└── requirements.txt               # Dependencies
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Set up virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run app.py
```
