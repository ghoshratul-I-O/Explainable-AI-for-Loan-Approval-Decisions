---
name: streamlit
description: >-
  Comprehensive guide, best practices, and templates for building, styling, debugging, running, and deploying interactive Streamlit data science and machine learning applications. Use when creating, running, troubleshooting, or deploying Streamlit apps.
---

# Streamlit Development & Deployment Skill

This skill provides expert workflows, performance patterns, and debugging procedures for interactive Python web dashboards using Streamlit.

---

## 1. Running and Managing Streamlit Applications

### Local Execution Command
Always run Streamlit pointing to the virtual environment interpreter:
```bash
.\.venv\Scripts\streamlit run app.py
```
Or when inside an activated environment:
```bash
streamlit run app.py
```

### Useful CLI Flags
- `--server.port 8501`: Specify local port.
- `--server.headless true`: Suppresses automatic browser window popups (for headless/remote setups).
- `--theme.base "light"` or `"dark"`: Sets theme.

---

## 2. Core Architecture Best Practices

### A. High-Performance Caching
Never reload large models or datasets on every user interaction:
- **`@st.cache_resource`**: Use for persistent objects (ML models, database connections, SHAP explainers).
- **`@st.cache_data`**: Use for pure data transformations (loading CSVs, dataframes, API responses).

```python
import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load("models/best_model.pkl")

model = load_model()
```

### B. Session State Management (`st.session_state`)
Preserves user input across widget reruns:
```python
if "applicant_data" not in st.session_state:
    st.session_state["applicant_data"] = {"loan_amount": 50000}
```

### C. Form Batching (`st.form`)
Avoid triggering full page reruns for each individual slider or text field:
```python
with st.form("loan_form"):
    loan_amt = st.number_input("Loan Amount")
    submit = st.form_submit_button("Submit")
```

---

## 3. Machine Learning & Explainable AI (SHAP) Integration

### Rendering Matplotlib & SHAP Plots
When displaying SHAP waterfall or beeswarm plots in Streamlit:
```python
import matplotlib.pyplot as plt
import shap
import streamlit as st

fig, ax = plt.subplots(figsize=(8, 4))
shap.plots.waterfall(shap_values[0], show=False)
plt.tight_layout()
st.pyplot(fig)
```

---

## 4. Deployment Workflow (Streamlit Community Cloud & GitHub)

1. **Repository Structure:**
   - Keep `app.py` at repository root or documented location.
   - Maintain `requirements.txt` listing all necessary libraries without local-only binaries.
   - Never commit heavy datasets (>25MB) to GitHub; package serialized models (`.pkl`) and lightweight summary JSONs.
2. **Deploy Steps:**
   - Push repository to GitHub.
   - Go to [share.streamlit.io](https://share.streamlit.io/).
   - Select repository, branch (`main`/`master`), and entry file (`app.py`).
   - Deploy!

