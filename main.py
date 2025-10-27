import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="KCB SmartCredit",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .risk-critical { color: #dc3545; font-weight: bold; }
    .risk-high { color: #fd7e14; font-weight: bold; }
    .risk-medium { color: #ffc107; font-weight: bold; }
    .risk-low { color: #28a745; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Sample data functions
def get_sample_npl_data():
    return pd.DataFrame({
        'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'npl_ratio': [8.5, 8.2, 7.9, 7.7, 7.8, 8.1, 8.4, 8.6, 8.3, 8.0, 7.8, 7.6]
    })

def get_sample_risk_distribution():
    return pd.DataFrame({
        'risk_band': ['Low', 'Medium', 'High', 'Critical'],
        'count': [845, 287, 89, 26]
    })

def get_sample_at_risk_loans():
    return pd.DataFrame({
        'Loan ID': ['LN001', 'LN002', 'LN003', 'LN004', 'LN005'],
        'Borrower': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sarah Wilson', 'David Brown'],
        'Risk Score': [92, 87, 84, 79, 76],
        'Outstanding (KES)': [450000, 280000, 150000, 320000, 185000],
        'Days Past Due': [45, 32, 28, 15, 12],
        'Risk Band': ['Critical', 'High', 'High', 'Medium', 'Medium'],
        'Action Required': ['Immediate Restructure', 'Contact & Restructure', 'Monitor Closely', 'Watch List', 'Watch List']
    })

def main():
    # Main header
    st.markdown('<div class="main-header">🏦 KCB SmartCredit - Credit Risk Management Platform</div>', unsafe_allow_html=True)
    
    # Quick stats row
    st.subheader("📈 Quick Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="NPL Ratio",
            value="8.2%",
            delta="-1.2%",
            delta_color="inverse"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="At-Risk Loans",
            value="47",
            delta="+3",
            delta_color="inverse"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Avg. Risk Score",
            value="62.3",
            delta="-4.1"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Recovery Rate",
            value="78.5%",
            delta="+5.2%"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Charts Section
    st.subheader("📊 Portfolio Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # NPL Trend Chart using native Streamlit
        st.write("📈 NPL Ratio Trend (12 Months)")
        npl_data = get_sample_npl_data()
        st.line_chart(npl_data, x='month', y='npl_ratio')
    
    with col2:
        # Risk Distribution using native Streamlit
        st.write("🎯 Risk Distribution Across Portfolio")
        risk_data = get_sample_risk_distribution()
        st.bar_chart(risk_data, x='risk_band', y='count')
    
    # At-Risk Loans Table
    st.subheader("🚨 Top At-Risk Loans Requiring Attention")
    
    at_risk_loans = get_sample_at_risk_loans()
    st.dataframe(at_risk_loans, use_container_width=True)
    
    # Recent Activity
    st.subheader("🕒 Recent System Activity")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Last Risk Model Update**\n\n2 hours ago")
    
    with col2:
        st.success("**Successful Restructures**\n\n12 this week")
    
    with col3:
        st.warning("**Pending Approvals**\n\n8 requests")

if __name__ == "__main__":
    main()
