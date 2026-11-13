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
- [ ] **Phase 4:** Model Training & Comparison (Logistic Regression, Decision Tree, Random Forest, XGBoost)
- [ ] **Phase 5:** Model Evaluation (ROC-AUC, PR-AUC, F1, Recall)
- [ ] **Phase 6:** Explainable AI (SHAP & LIME)
- [ ] **Phase 7:** Fairness & Bias Analysis (Fairlearn)
- [ ] **Phase 8:** Dashboard Development (Streamlit)
- [ ] **Phase 9:** Deployment & Documentation (Streamlit Cloud, GitHub)

## Current Active Phase
- **Phase 4:** Model Training and Comparison (`notebooks/Model_Training.ipynb`).

## Session Progress & Resume Checkpoint
- **Status:** Phase 2 and Phase 3 completed. Engineered dataset ready at `data/train_features.csv` (233,154 rows × 44 numeric features, 0 nulls).
- **Immediate Next Action:** Initialize Phase 4 (`notebooks/Model_Training.ipynb`) to implement stratified train-test split, scale features, train 4 benchmark models (Logistic Regression, Decision Tree, Random Forest, XGBoost), and compare baseline ROC-AUC / PR-AUC scores.
