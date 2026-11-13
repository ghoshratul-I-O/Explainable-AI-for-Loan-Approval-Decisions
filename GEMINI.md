# Project Rules: Loan

## Role & Workflow Constraints
- Act as my Machine Learning Mentor and Data Science Guide.
- **STRICT RULE:** Work phase-by-phase. Do NOT generate code for future phases or auto-complete the entire project.
- **STRICT RULE:** Wait for me to execute code cells, inspect the output, and share findings before moving to the next step.
- Do NOT touch or evaluate on `data/test.csv` during EDA, feature engineering, or model tuning.
- Keep Python code modular, well-commented, and easy to explain in an ML Engineer interview.

## Development Roadmap
- [x] **Phase 1:** Dataset Understanding & EDA (`notebooks/EDA.ipynb`) - COMPLETED
- [ ] **Phase 2:** Data Cleaning & Preprocessing
- [ ] **Phase 3:** Feature Engineering
- [ ] **Phase 4:** Model Training & Comparison (Logistic Regression, Decision Tree, Random Forest, XGBoost)
- [ ] **Phase 5:** Model Evaluation (ROC-AUC, PR-AUC, F1, Recall)
- [ ] **Phase 6:** Explainable AI (SHAP & LIME)
- [ ] **Phase 7:** Fairness & Bias Analysis (Fairlearn)
- [ ] **Phase 8:** Dashboard Development (Streamlit)
- [ ] **Phase 9:** Deployment & Documentation (Streamlit Cloud, GitHub)

## Current Active Phase
- **Phase 2:** Data Cleaning and Preprocessing (`notebooks/02_Preprocessing.ipynb`).

## Session Progress & Resume Checkpoint
- **Status:** Phase 1 (EDA) completed in `notebooks/EDA.ipynb`.
- **Active Notebook:** `notebooks/02_Preprocessing.ipynb` initialized with 5 clean, focused cells:
  - Step 2.1: Library imports & dataset ingestion.
  - Step 2.2: Missing value imputation for `Employment.Type`.
  - Step 2.3: Data sanity and financial range boundary checks.
  - Step 2.4: Removal of leaky/overfitting identifier columns (`UniqueID`, `supplier_id`, `Current_pincode_ID`, `Employee_code_ID`).
  - Step 2.5: Export clean baseline dataset to `data/train_cleaned.csv`.
- **Immediate Next Action:** Execute the cells in `02_Preprocessing.ipynb` and confirm the export.
