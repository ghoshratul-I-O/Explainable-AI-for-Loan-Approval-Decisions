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
- [ ] **Phase 7:** Fairness & Bias Analysis (Fairlearn)
- [ ] **Phase 8:** Dashboard Development (Streamlit)
- [ ] **Phase 9:** Deployment & Documentation (Streamlit Cloud, GitHub)

## Current Active Phase
- **Phase 7:** Fairness and Bias Analysis (`notebooks/Fairness_Analysis.ipynb`).

## Session Progress & Resume Checkpoint
- **Status:** Phase 6 (Explainable AI) successfully executed in `notebooks/Explainable_AI.ipynb`. Both SHAP (Global Beeswarm, Feature Importance, Local Waterfall) and LIME rule-based surrogate explanations generated.
- **Immediate Next Action:** Initialize Phase 7 (`notebooks/Fairness_Analysis.ipynb`) using Fairlearn to audit algorithmic fairness and demographic parity across sensitive applicant segments (e.g., employment type, geography, age groups).
