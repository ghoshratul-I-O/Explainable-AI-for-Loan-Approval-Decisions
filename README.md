# Explainable AI for Loan Default Prediction

An end-to-end Machine Learning project to predict vehicle loan default risk and interpret predictions using Explainable AI (SHAP, LIME), fairness auditing, and an interactive Streamlit application.

**Dataset:** LTFS Vehicle Loan Default Prediction (India)  
**Objective:** Predict the likelihood of loan default and explain the primary drivers behind each individual decision.

---

## Development Roadmap & Status

| Phase | Task | Tools / Methods | Status |
| :--- | :--- | :--- | :---: |
| **Phase 1** | **Dataset Understanding & EDA** | Pandas, Matplotlib, Seaborn | ✅ COMPLETED |
| **Phase 2** | **Data Cleaning & Preprocessing** | Outlier handling, leaky ID removal, imputation | ✅ COMPLETED |
| **Phase 3** | **Feature Engineering** | Age derivation, tenure parsing, NTC flag, bureau tiers | ✅ COMPLETED |
| **Phase 4** | **Model Training & Comparison** | Logistic Regression, Decision Tree, Random Forest, XGBoost | ✅ COMPLETED |
| **Phase 5** | **Model Evaluation & Threshold Tuning** | Precision, Recall, F1, ROC-AUC, PR-AUC, Threshold Curves | ✅ COMPLETED |
| **Phase 6** | **Explainable AI (XAI)** | SHAP (Global Beeswarm & Local Waterfall), LIME | ✅ COMPLETED |
| **Phase 7** | **Fairness & Bias Analysis** | Fairlearn (Demographic Parity, Equalized Opportunity) | ✅ COMPLETED |
| **Phase 8** | **Dashboard Development** | Streamlit (`app.py`), SHAP integration, What-If Simulator | ✅ COMPLETED |
| **Phase 9** | **Deployment & Documentation** | Streamlit Community Cloud, GitHub | 🚀 READY |

---

## Model Benchmark Results

Evaluated on 46,631 held-out validation applicants (stratified 80/20 split):

| Model | ROC-AUC | PR-AUC | Default Recall | Default Precision | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **XGBoost (Champion)** | **0.6561** | **0.3314** | **64.89%** | **29.73%** | **0.4078** |
| Random Forest | 0.6441 | 0.3168 | 62.15% | 28.50% | 0.3990 |
| Logistic Regression | 0.6313 | 0.2985 | 60.80% | 27.20% | 0.3900 |
| Decision Tree | 0.6186 | 0.2810 | 58.40% | 26.10% | 0.3900 |

- **Optimal F1 Decision Threshold:** `0.4846` ($\approx 0.50$ baseline).
- **Champion Model Artifacts:** Serialized in `models/best_model.pkl` with `scaler.pkl` and `feature_names.pkl`.

---

## Explainable AI & Fairness Highlights

1. **Top Risk Drivers (SHAP Beeswarm):**
   - High `ltv` (>80% leverage) significantly escalates default probability.
   - High `PERFORM_CNS.SCORE` strongly pulls default risk downward.
   - High `NO.OF_INQUIRIES` (credit hunger) signals acute default risk.
2. **Local Interpretability (SHAP Waterfall):**
   - Computes individualized adverse action explanations for each customer.
3. **Algorithmic Fairness (Fairlearn Audit):**
   - **Employment Type Parity Ratio:** `0.8664` (Safely passes the regulatory **80% Rule**).
   - Audited thin-file vulnerability for young borrowers (<25 years).

---

## Interactive Streamlit Application (`app.py`)

The application features:
1. **Portfolio Risk Dashboard:** High-level KPIs and risk distributions.
2. **Real-time Loan Predictor:** Instant risk probability with color-coded underwriting badges.
3. **SHAP Waterfall Visualizer:** Dynamic explanation of individual credit decisions.
4. **What-If Simulator:** Interactive sliders demonstrating how adding down payment or improving credit scores flips a decision from **Flagged $\longrightarrow$ Approved**.

### Launching Locally:
```bash
# Navigate to the Loan project folder
cd Loan

# Run Streamlit
.\.venv\Scripts\streamlit run app.py
```

---

## Project Structure

```text
Loan/
├── data/
│   ├── train.csv                      # Raw training data (233,154 records)
│   ├── test.csv                       # Test set (held-out)
│   ├── train_cleaned.csv              # Phase 2 output (0 nulls, clean IDs)
│   ├── train_features.csv             # Phase 3 ML-ready feature matrix
│   └── data_dictionary.md             # Complete schema reference
├── notebooks/
│   ├── EDA.ipynb                      # Phase 1: Exploratory Data Analysis
│   ├── Preprocessing.ipynb            # Phase 2: Data Cleaning
│   ├── Feature_Engineering.ipynb      # Phase 3: Feature Engineering
│   ├── Model_Training.ipynb           # Phase 4 & 5: Training, Evaluation & Tuning
│   ├── Explainable_AI.ipynb           # Phase 6: SHAP & LIME
│   └── Fairness_Analysis.ipynb        # Phase 7: Fairlearn Audit
├── models/
│   ├── best_model.pkl                 # Champion XGBoost pipeline
│   ├── scaler.pkl                     # Standard scaler
│   ├── feature_names.pkl              # 43 feature names list
│   ├── feature_defaults.json          # Median background values for app
│   └── portfolio_summary.json         # Precomputed dashboard KPIs
├── app.py                             # Interactive Streamlit dashboard
├── requirements.txt                   # Project dependencies
├── .gitignore                         # Excludes large data & environments
├── GEMINI.md                          # Phase tracking & rules
└── README.md                          # Comprehensive project documentation
```
