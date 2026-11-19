# Project Rules: Loan

## Role & Workflow Constraints
- Act as my Machine Learning Mentor and Data Science Guide.
- **STRICT RULE:** Work phase-by-phase. Do NOT generate code for future phases or auto-complete the entire project.
- **STRICT RULE:** Wait for me to execute code cells, inspect the output, and share findings before moving to the next step.
- Do NOT touch or evaluate on `data/test.csv` during EDA, feature engineering, or model tuning.
- Keep Python code modular, well-commented, and easy to explain in an ML Engineer interview.

## Development Roadmap
- [x] **Phase 1:** Dataset Understanding & EDA (`notebooks/EDA.ipynb`) - COMPLETED
- [x] **Phase 2:** Data Cleaning & Preprocessing (`notebooks/Preprocessing.ipynb`) - COMPLETED
- [x] **Phase 3:** Feature Engineering (`notebooks/Feature_Engineering.ipynb`) - COMPLETED
- [x] **Phase 4:** Model Training & Comparison (Logistic Regression, Decision Tree, Random Forest, XGBoost) - COMPLETED
- [x] **Phase 5:** Model Evaluation & Threshold Tuning (Confusion Matrix, PR Curve, Optimal Threshold ~0.485) - COMPLETED
- [x] **Phase 6:** Explainable AI (SHAP Global Beeswarm, Local Waterfall, LIME Surrogates) - COMPLETED
- [x] **Phase 7:** Fairness & Bias Analysis (Fairlearn Demographic Parity, Age & Employment Audits) - COMPLETED
- [ ] **Phase 8:** Dashboard Development (Streamlit `app.py`)
- [ ] **Phase 9:** Deployment & Documentation (Streamlit Cloud, GitHub)

## Current Active Phase
- **Phase 8:** Dashboard Development (`app.py`).

## Session Progress & Resume Checkpoint
- **Status:** Phase 7 (Fairness & Bias Analysis) completed. Audited employment disparity (Ratio 0.8664, passed 80% rule) and age bracket vulnerability in `notebooks/Fairness_Analysis.ipynb`.
- **Immediate Next Action:** Build the interactive multi-page Streamlit web application (`app.py`) featuring:
  1. **Portfolio Risk Dashboard:** High-level metrics, loan default statistics, and risk charts.
  2. **Loan Prediction Engine:** Applicant input form with instant probability score and decision outcome.
  3. **Explainable AI (SHAP):** Live waterfall/force plot explaining the applicant's prediction.
  4. **Interactive What-If Simulator:** Dynamic sliders to test parameter changes (e.g. down payment, bureau score).
