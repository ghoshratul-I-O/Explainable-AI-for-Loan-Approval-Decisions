# Comprehensive Project Report: Explainable AI for Loan Default Prediction

**Student / Researcher:** Ratul  
**Domain:** Financial Risk Analytics & Explainable Machine Learning  
**Dataset:** LTFS Vehicle Loan Default Prediction (India) — 233,154 records  

---

## 1. Executive Summary
Predicting default risk in vehicle loan financing is critical for non-banking financial companies (NBFCs). When a customer defaults on their first EMI, recovery costs and asset depreciation cause severe capital write-downs. This project develops an end-to-end Machine Learning pipeline that predicts default risk with high recall while providing full transparency via Explainable AI (SHAP and LIME) and auditing for algorithmic demographic fairness (Fairlearn).

---

## 2. Dataset Understanding & Exploratory Data Analysis (EDA)
- **Portfolio Size:** 233,154 borrower records across 41 raw features.
- **Class Imbalance:** 78.29% Non-Defaults ($n=182,543$) vs. 21.71% Defaults ($n=50,611$). This ~3.6:1 imbalance demonstrates that naive accuracy is deceptive; models must optimize for ROC-AUC, Recall, and PR-AUC.
- **Key Empirical Risk Drivers:**
  - **Loan-to-Value (LTV):** Default probability climbs steadily from 15.0% (<66% LTV) to 26.6% (>84% LTV).
  - **Credit Bureau Score:** Over 50.16% of borrowers have 0 bureau score ("No Bureau History Available"), representing thin-file first-time borrowers.
  - **Credit Inquiries:** Borrowers with 4+ inquiries in the last 6 months default at 34.9% (vs. 21.1% for 0 inquiries), highlighting severe credit hunger.

---

## 3. Data Cleaning & Feature Engineering
1. **Missing Imputation:** Only `Employment.Type` contained missing values (~3.3%). Imputed as an explicit `'Missing'` category to preserve applicant non-disclosure signals.
2. **Leakage & Overfitting Prevention:** Dropped arbitrary primary keys (`UniqueID`) and high-cardinality noise IDs (`supplier_id`, `Current_pincode_ID`, `Employee_code_ID`).
3. **Engineered Predictors:**
   - `age`: Applicant age at disbursal derived from two-digit year parsing (18 to 69 years).
   - `avg_acct_age_months` & `credit_hist_len_months`: Converted duration text strings (`'1yrs 11mon'`) into continuous integer months.
   - `is_new_to_credit`: Binary flag separating unrated borrowers from bad-credit borrowers.
   - `down_payment`: Borrower equity invested (`asset_cost - disbursed_amount`).
   - `bureau_risk_tier`: Consolidated 20 verbose CRISIL descriptions into 6 standardized risk tiers.

---

## 4. Model Training & Comparison Leaderboard

Evaluated on 46,631 held-out validation applicants using a stratified 80/20 split:

| Model | ROC-AUC | PR-AUC | Default Recall | Default Precision | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **XGBoost (Champion)** | **0.6561** | **0.3314** | **64.89%** | **29.73%** | **0.4078** |
| Random Forest | 0.6441 | 0.3168 | 62.15% | 28.50% | 0.3990 |
| Logistic Regression | 0.6313 | 0.2985 | 60.80% | 27.20% | 0.3900 |
| Decision Tree | 0.6186 | 0.2810 | 58.40% | 26.10% | 0.3900 |

---

## 5. Decision Threshold Optimization
- **Baseline (Threshold = 0.50):** Recall: 64.9%, Precision: 29.7%, F1: 0.4078.
- **Mathematical Optimal F1 (Threshold = 0.4846):** Peak F1: 0.4099.
- **Two-Tier Operational Recommendation:**
  - $P < 0.35 \rightarrow$ Auto-Approve (Prime borrower).
  - $0.35 \le P < 0.50 \rightarrow$ Manual Underwriting Review (Request guarantor/income proof).
  - $P \ge 0.50 \rightarrow$ High-Risk Flag (Require 25%+ down payment).

---

## 6. Explainable AI (SHAP & LIME)
- **Global Interpretability:** SHAP TreeExplainer confirms `ltv`, `PERFORM_CNS.SCORE`, `disbursed_amount`, and `NO.OF_INQUIRIES` as the primary portfolio risk drivers.
- **Local Interpretability:** SHAP Waterfall and LIME surrogate rules provide customer-facing adverse action reasons (e.g. flagging an applicant specifically due to high leverage and recent loan inquiries).

---

## 7. Algorithmic Fairness Audit (Fairlearn)
- **Employment Type Parity Ratio:** `0.8664` $\ge 0.80$, officially satisfying the **Four-Fifths (80%) Fair Lending Rule**.
- **Age Disparity:** Identified thin-file false alarms for young applicants (<25 years), recommending alternative credit data integration.

---

## 8. Interactive Streamlit Web Application (`app.py`)
- Fully decoupled from 60 MB raw datasets; loads serialized artifacts in <300 KB.
- Implements 4 core modules: Portfolio Dashboard, Loan Predictor, SHAP Waterfall Explainer, and Counterfactual What-If Simulator.
