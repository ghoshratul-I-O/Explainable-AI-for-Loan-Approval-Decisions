import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path
import matplotlib.pyplot as plt
import shap
import warnings

warnings.filterwarnings('ignore')

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Explainable AI - Loan Default Risk",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (CSS Injection)
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: #F8FAFC;
        padding: 1.1rem;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 1rem;
    }
    .risk-badge-low {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 700;
        display: inline-block;
        font-size: 1.05rem;
    }
    .risk-badge-med {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 700;
        display: inline-block;
        font-size: 1.05rem;
    }
    .risk-badge-high {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 700;
        display: inline-block;
        font-size: 1.05rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# High-Performance Caching: Model & Metadata
# ---------------------------------------------------------
@st.cache_resource(show_spinner="Loading ML models & explainers...")
def load_model_artifacts():
    base_path = Path(__file__).parent if "__file__" in locals() else Path(".")
    models_dir = base_path / "models" if (base_path / "models").exists() else Path("models")
    
    model = joblib.load(models_dir / "best_model.pkl")
    feature_names = joblib.load(models_dir / "feature_names.pkl")
    
    with open(models_dir / "feature_defaults.json", "r") as f:
        feature_defaults = json.load(f)
        
    with open(models_dir / "portfolio_summary.json", "r") as f:
        portfolio_summary = json.load(f)
        
    explainer = shap.TreeExplainer(model)
    return model, feature_names, feature_defaults, portfolio_summary, explainer

model, feature_names, feature_defaults, portfolio_summary, explainer = load_model_artifacts()

# ---------------------------------------------------------
# Sidebar Configuration
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/bank-building.png", width=64)
    st.title("Credit Risk Console")
    st.markdown("**LTFS Vehicle Loan Underwriting**")
    st.divider()
    
    st.subheader("⚙️ Decision Threshold")
    threshold = st.slider(
        "Default Cutoff Threshold",
        min_value=0.30,
        max_value=0.70,
        value=0.50,
        step=0.05,
        help="Applicants with predicted default probability >= cutoff are flagged as high risk."
    )
    if threshold < 0.45:
        st.info("🛡️ **Loss Minimization (Conservative):** Maximizes default recall, intercepts more defaulters.")
    elif threshold > 0.55:
        st.warning("🚀 **Growth Mode (Aggressive):** Higher precision, fewer false alarms, higher approval rate.")
    else:
        st.success("⚖️ **Balanced Baseline:** Peak F1-score (~0.41).")
        
    st.divider()
    st.markdown("""
    **Model Specs:**
    - Algorithm: **XGBoost Classifier**
    - Val ROC-AUC: **0.656**
    - Features: **43 attributes**
    - Framework: **SHAP & Fairlearn**
    """)

# Main Header
st.markdown('<div class="main-title">Explainable AI: Vehicle Loan Default Risk</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Real-time risk scoring, transparent credit underwriting, and interactive SHAP decision explanations.</div>', unsafe_allow_html=True)

# Main Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Portfolio Risk Dashboard",
    "🔍 Loan Prediction Engine",
    "🧠 Explainable AI (SHAP)",
    "⚡ Interactive What-If Simulator"
])

# ---------------------------------------------------------
# TAB 1: Portfolio Risk Dashboard
# ---------------------------------------------------------
with tab1:
    st.subheader("Portfolio Health & Benchmark Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Loan Portfolio", f"{portfolio_summary['total_loans']:,}")
    col2.metric("Baseline Default Rate", f"{portfolio_summary['overall_default_rate']:.2f}%")
    col3.metric("Average Loan Disbursed", f"₹{portfolio_summary['avg_disbursed_amount']:,.0f}")
    col4.metric("Average LTV Leverage", f"{portfolio_summary['avg_ltv']:.1f}%")
    
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Default Risk by Employment Type")
        emp_data = portfolio_summary['default_by_employment']
        fig1, ax1 = plt.subplots(figsize=(6, 3.5))
        bars1 = ax1.bar(emp_data.keys(), emp_data.values(), color=['#2b5c8f', '#d95f02', '#7570b3'], width=0.45)
        ax1.set_ylabel("Default Rate (%)")
        ax1.axhline(portfolio_summary['overall_default_rate'], color='black', linestyle='--', label='Portfolio Avg (21.7%)')
        for bar in bars1:
            yval = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.4, f"{yval:.1f}%", ha='center', fontweight='bold')
        ax1.set_ylim(0, 30)
        ax1.legend(loc='lower right')
        st.pyplot(fig1)
        plt.close(fig1)
        
    with c2:
        st.markdown("#### Default Risk by Number of Loan Inquiries")
        inq_data = portfolio_summary['default_by_inquiries']
        fig2, ax2 = plt.subplots(figsize=(6, 3.5))
        bars2 = ax2.bar(inq_data.keys(), inq_data.values(), color='#e7298a', width=0.45)
        ax2.set_ylabel("Default Rate (%)")
        ax2.set_xlabel("Number of Inquiries in Last 6 Months")
        for bar in bars2:
            yval = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval:.1f}%", ha='center', fontweight='bold')
        ax2.set_ylim(0, 40)
        st.pyplot(fig2)
        plt.close(fig2)

# ---------------------------------------------------------
# Helper function: Vector Builder
# ---------------------------------------------------------
def build_feature_vector(input_dict):
    data = feature_defaults.copy()
    data.update(input_dict)
    
    # Auto-derive financial leverage & equity
    data['ltv'] = (data['disbursed_amount'] / data['asset_cost']) * 100
    data['down_payment'] = data['asset_cost'] - data['disbursed_amount']
    data['is_new_to_credit'] = 1 if data['PERFORM_CNS.SCORE'] == 0 else 0
    
    # One-hot encoding mappings
    data['Employment.Type_Salaried'] = 1 if data.get('emp_type') == 'Salaried' else 0
    data['Employment.Type_Self employed'] = 1 if data.get('emp_type') == 'Self employed' else 0
    
    # Bureau tier mapping
    score = data['PERFORM_CNS.SCORE']
    data['bureau_risk_tier_Very Low'] = 1 if (score >= 700) else 0
    data['bureau_risk_tier_Low'] = 1 if (600 <= score < 700) else 0
    data['bureau_risk_tier_Medium'] = 1 if (450 <= score < 600) else 0
    data['bureau_risk_tier_Very High'] = 1 if (1 <= score < 350) else 0
    data['bureau_risk_tier_No History'] = 1 if (score == 0) else 0
    
    df_row = pd.DataFrame([data])
    return df_row[feature_names]

# Initialize applicant session state
if "applicant_input" not in st.session_state:
    st.session_state["applicant_input"] = {
        'asset_cost': 75000,
        'disbursed_amount': 55000,
        'age': 32,
        'emp_type': 'Salaried',
        'PERFORM_CNS.SCORE': 650,
        'NO.OF_INQUIRIES': 0,
        'PRI.OVERDUE.ACCTS': 0,
        'DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS': 0,
        'Aadhar_flag': 1,
        'PAN_flag': 1
    }

# ---------------------------------------------------------
# TAB 2: Loan Prediction Engine
# ---------------------------------------------------------
with tab2:
    st.subheader("New Loan Application Assessment")
    st.caption("Enter customer details to generate an instantaneous credit risk assessment.")
    
    # Presets
    preset = st.selectbox(
        "Load Quick Benchmark Profile:",
        ["Current / Custom Entry", "Safe Prime Borrower (Low Risk)", "Thin-File / First-Time Buyer", "High-Risk Over-Leveraged"]
    )
    
    if preset == "Safe Prime Borrower (Low Risk)":
        st.session_state["applicant_input"].update({
            'asset_cost': 85000, 'disbursed_amount': 50000, 'age': 38,
            'emp_type': 'Salaried', 'PERFORM_CNS.SCORE': 750, 'NO.OF_INQUIRIES': 0,
            'PRI.OVERDUE.ACCTS': 0, 'DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS': 0
        })
    elif preset == "Thin-File / First-Time Buyer":
        st.session_state["applicant_input"].update({
            'asset_cost': 70000, 'disbursed_amount': 58000, 'age': 23,
            'emp_type': 'Self employed', 'PERFORM_CNS.SCORE': 0, 'NO.OF_INQUIRIES': 1,
            'PRI.OVERDUE.ACCTS': 0, 'DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS': 0
        })
    elif preset == "High-Risk Over-Leveraged":
        st.session_state["applicant_input"].update({
            'asset_cost': 65000, 'disbursed_amount': 59000, 'age': 29,
            'emp_type': 'Self employed', 'PERFORM_CNS.SCORE': 380, 'NO.OF_INQUIRIES': 4,
            'PRI.OVERDUE.ACCTS': 2, 'DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS': 1
        })

    # Input Form (Prevents premature reruns)
    with st.form("loan_application_form"):
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("##### 🚗 Loan & Vehicle Details")
            asset_cost = st.number_input("Vehicle Cost (₹)", min_value=30000, max_value=500000, value=int(st.session_state["applicant_input"]['asset_cost']), step=5000)
            disbursed_amount = st.number_input("Requested Loan Amount (₹)", min_value=15000, max_value=int(asset_cost), value=int(min(st.session_state["applicant_input"]['disbursed_amount'], asset_cost)), step=5000)
            calc_ltv = (disbursed_amount / asset_cost) * 100
            calc_dp = asset_cost - disbursed_amount
            st.info(f"**LTV Leverage:** {calc_ltv:.1f}%\n\n**Down Payment:** ₹{calc_dp:,.0f}")
            
        with c2:
            st.markdown("##### 👤 Borrower Demographics")
            age = st.slider("Borrower Age (Years)", min_value=18, max_value=70, value=int(st.session_state["applicant_input"]['age']))
            emp_type = st.selectbox("Employment Type", ["Salaried", "Self employed", "Missing"], index=0 if st.session_state["applicant_input"]['emp_type'] == 'Salaried' else 1)
            aadhar = st.checkbox("Aadhaar Card Submitted", value=bool(st.session_state["applicant_input"]['Aadhar_flag']))
            pan = st.checkbox("PAN Card Submitted", value=bool(st.session_state["applicant_input"]['PAN_flag']))
            
        with c3:
            st.markdown("##### 📈 Credit History & Bureau")
            cns_score = st.slider("CRISIL/HighMark Bureau Score (0 = No History)", min_value=0, max_value=890, value=int(st.session_state["applicant_input"]['PERFORM_CNS.SCORE']), step=10)
            inquiries = st.number_input("Recent Credit Inquiries (Past 6 Mos)", min_value=0, max_value=15, value=int(st.session_state["applicant_input"]['NO.OF_INQUIRIES']))
            overdue_accts = st.number_input("Past Overdue Accounts Count", min_value=0, max_value=10, value=int(st.session_state["applicant_input"]['PRI.OVERDUE.ACCTS']))
            delinquent_6m = st.number_input("Delinquent Accounts (Last 6 Mos)", min_value=0, max_value=5, value=int(st.session_state["applicant_input"]['DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS']))
            
        submit_btn = st.form_submit_button("⚡ Assess Default Risk", use_container_width=True)
        
    if submit_btn:
        st.session_state["applicant_input"] = {
            'asset_cost': asset_cost,
            'disbursed_amount': disbursed_amount,
            'age': age,
            'emp_type': emp_type,
            'PERFORM_CNS.SCORE': cns_score,
            'NO.OF_INQUIRIES': inquiries,
            'PRI.OVERDUE.ACCTS': overdue_accts,
            'DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS': delinquent_6m,
            'Aadhar_flag': int(aadhar),
            'PAN_flag': int(pan)
        }
        
    # Evaluate current applicant
    current_vec = build_feature_vector(st.session_state["applicant_input"])
    prob_default = float(model.predict_proba(current_vec)[0, 1])
    is_default_flagged = prob_default >= threshold
    
    st.markdown("---")
    res_c1, res_c2, res_c3 = st.columns([1, 1, 1.8])
    
    with res_c1:
        st.metric("Predicted Default Probability", f"{prob_default:.1%}")
        st.progress(min(max(prob_default, 0.0), 1.0))
    with res_c2:
        st.metric("Current Decision Cutoff", f"{threshold:.1%}")
    with res_c3:
        st.markdown("#### Underwriting Decision")
        if prob_default < 0.35:
            st.markdown('<div class="risk-badge-low">✅ APPROVED: Low Risk Prime Customer</div>', unsafe_allow_html=True)
            st.caption("Standard interest rate & rapid disbursal eligible.")
        elif prob_default < threshold:
            st.markdown('<div class="risk-badge-med">⚠️ UNDERWRITING REVIEW: Moderate Risk</div>', unsafe_allow_html=True)
            st.caption("Approved subject to standard address verification and salary slip confirmation.")
        else:
            st.markdown('<div class="risk-badge-high">🛑 FLAGGED / HIGH RISK: Default Alert</div>', unsafe_allow_html=True)
            st.caption("Counter-offer required: request a 10%+ higher down payment or guarantor.")

    # Export report download button
    report_text = f"""--- LOAN UNDERWRITING REPORT ---
Vehicle Cost: INR {st.session_state['applicant_input']['asset_cost']:,}
Disbursed Loan: INR {st.session_state['applicant_input']['disbursed_amount']:,}
LTV Ratio: {current_vec['ltv'].iloc[0]:.2f}%
Bureau Score: {st.session_state['applicant_input']['PERFORM_CNS.SCORE']}
Employment Type: {st.session_state['applicant_input']['emp_type']}
Predicted Default Probability: {prob_default:.2%}
Decision Cutoff Threshold: {threshold:.2%}
Outcome: {'FLAGGED / HIGH RISK' if is_default_flagged else 'APPROVED / PASS'}
"""
    st.download_button(
        label="📄 Download Assessment Memo (.txt)",
        data=report_text,
        file_name=f"credit_assessment_{st.session_state['applicant_input']['age']}yo_{prob_default:.0%}.txt",
        mime="text/plain"
    )

# ---------------------------------------------------------
# TAB 3: Explainable AI (SHAP)
# ---------------------------------------------------------
with tab3:
    st.subheader("Explainable AI: Adverse Action Breakdown")
    st.markdown("Under Fair Lending guidelines, models cannot act as black boxes. This **SHAP Waterfall Plot** explains the exact decision path for the applicant assessed in Tab 2.")
    
    active_vec = build_feature_vector(st.session_state["applicant_input"])
    shap_val = explainer(active_vec)
    curr_prob = float(model.predict_proba(active_vec)[0, 1])
    
    fig3, ax3 = plt.subplots(figsize=(9, 5))
    shap.plots.waterfall(shap_val[0], max_display=10, show=False)
    plt.title(f"SHAP Waterfall: Prediction Path (P = {curr_prob:.1%})", fontsize=12, pad=10)
    plt.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)
    
    st.markdown("#### 🔍 Plain-English Decision Drivers")
    shap_series = pd.Series(shap_val[0].values, index=feature_names).sort_values()
    top_protective = shap_series.head(3)
    top_risk = shap_series.tail(3)
    
    e1, e2 = st.columns(2)
    with e1:
        st.success("**Top Factors Decreasing Risk (Protective):**")
        for f, val in top_protective.items():
            st.write(f"- `{f}` : **{val:.3f}** log-odds")
    with e2:
        st.error("**Top Factors Increasing Risk (Red Flags):**")
        for f, val in top_risk.items():
            st.write(f"- `{f}` : **+{val:.3f}** log-odds")

# ---------------------------------------------------------
# TAB 4: Interactive What-If Simulator
# ---------------------------------------------------------
with tab4:
    st.subheader("Counterfactual 'What-If' Simulation")
    st.markdown("If a loan application was rejected or flagged, what specific changes would make it creditworthy? Adjust the parameters below to observe real-time risk reduction.")
    
    base_dict = st.session_state["applicant_input"].copy()
    base_vec = build_feature_vector(base_dict)
    base_prob = float(model.predict_proba(base_vec)[0, 1])
    
    sim_c1, sim_c2 = st.columns(2)
    
    with sim_c1:
        st.markdown("#### Adjust Parameters")
        sim_dp_add = st.slider("Increase Down Payment by (₹)", 0, 40000, 15000, step=5000)
        sim_score_add = st.slider("Improve Bureau Score by (Points)", 0, 200, 50, step=25)
        sim_delinq_fix = st.checkbox("Resolve Past Delinquencies (Set to 0)", value=True)
        
    # Simulate modified profile
    sim_dict = base_dict.copy()
    sim_dict['disbursed_amount'] = max(10000, base_dict['disbursed_amount'] - sim_dp_add)
    sim_dict['PERFORM_CNS.SCORE'] = min(850, base_dict['PERFORM_CNS.SCORE'] + sim_score_add)
    if sim_delinq_fix:
        sim_dict['DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS'] = 0
        sim_dict['PRI.OVERDUE.ACCTS'] = 0
        
    sim_vec = build_feature_vector(sim_dict)
    sim_prob = float(model.predict_proba(sim_vec)[0, 1])
    risk_reduction = base_prob - sim_prob
    
    with sim_c2:
        st.markdown("#### Impact Analysis")
        st.metric(
            label="Simulated Default Probability",
            value=f"{sim_prob:.1%}",
            delta=f"{-risk_reduction:.1%} Risk Change",
            delta_color="inverse"
        )
        
        st.write(f"**Original Risk:** {base_prob:.1%}  →  **Simulated Risk:** {sim_prob:.1%}")
        
        if sim_prob < threshold and base_prob >= threshold:
            st.success("🎉 **Success!** This counterfactual adjustment flips the loan decision from **Flagged → Approved**!")
        elif sim_prob < threshold:
            st.info("Loan remains within the Approved zone.")
        else:
            st.warning("Even with these adjustments, additional collateral or down-payment is needed to clear the threshold.")
