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
- [ ] **Phase 6:** Explainable AI (SHAP & LIME)
- [ ] **Phase 7:** Fairness & Bias Analysis (Fairlearn)
- [ ] **Phase 8:** Dashboard Development (Streamlit)
- [ ] **Phase 9:** Deployment & Documentation (Streamlit Cloud, GitHub)

## Current Active Phase
- **Phase 6:** Explainable AI (`notebooks/Explainable_AI.ipynb`).

## Session Progress & Resume Checkpoint
- **Status:** Phase 4 and Phase 5 completed. Best model (XGBoost, ROC-AUC 0.656, Max F1 0.4099 @ threshold ~0.485) and feature artifacts saved in `models/`.
- **Immediate Next Action:** Initialize Phase 6 (`notebooks/Explainable_AI.ipynb`) to compute SHAP TreeExplainer, global feature summary plots, local borrower decision waterfall plots, and LIME explanations.
