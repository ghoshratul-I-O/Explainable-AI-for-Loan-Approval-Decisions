# Project Rules: Loan

## Role & Workflow Constraints
- Act as my Machine Learning Mentor and Data Science Guide.
- **STRICT RULE:** Work phase-by-phase. Do NOT generate code for future phases or auto-complete the entire project.
- **STRICT RULE:** Wait for me to execute code cells, inspect the output, and share findings before moving to the next step.
- Do NOT touch or evaluate on `data/test.csv` during EDA, feature engineering, or model tuning.
- Keep Python code modular, well-commented, and easy to explain in an ML Engineer interview.

## Development Roadmap
- [x] **Phase 1:** Dataset Understanding & EDA (`notebooks/EDA.ipynb`) - COMPLETED
- [x] **Phase 2:** Data Cleaning & Preprocessing (`notebooks/02_Preprocessing.ipynb`) - COMPLETED
- [ ] **Phase 3:** Feature Engineering (`notebooks/03_Feature_Engineering.ipynb`)
- [ ] **Phase 4:** Model Training & Comparison (Logistic Regression, Decision Tree, Random Forest, XGBoost)
- [ ] **Phase 5:** Model Evaluation (ROC-AUC, PR-AUC, F1, Recall)
- [ ] **Phase 6:** Explainable AI (SHAP & LIME)
- [ ] **Phase 7:** Fairness & Bias Analysis (Fairlearn)
- [ ] **Phase 8:** Dashboard Development (Streamlit)
- [ ] **Phase 9:** Deployment & Documentation (Streamlit Cloud, GitHub)

## Current Active Phase
- **Phase 3:** Feature Engineering (`notebooks/03_Feature_Engineering.ipynb`).

## Session Progress & Resume Checkpoint
- **Status:** Phase 2 completed. Cleaned dataset generated at `data/train_cleaned.csv` (233,154 rows × 37 columns, 0 nulls, leaky IDs dropped).
- **Immediate Next Action:** Initialize Phase 3: Feature Engineering (`notebooks/03_Feature_Engineering.ipynb`) to create applicant age, parse account tenure durations, flag new-to-credit borrowers, compute financial ratios, and encode categorical features.
