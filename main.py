import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
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
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Sample data functions
def get_sample_npl_data():
    return pd.DataFrame({
        'month': pd.date_range('2023-01-01', periods=12, freq='M'),
        'npl_ratio': [8.5, 8.2, 7.9, 7.7, 7.8, 8.1, 8.4, 8.6, 8.3, 8.0, 7.8, 7.6]
    })

def get_sample_risk_distribution():
    return pd.DataFrame({
        'risk_band': ['Low', 'Medium', 'High', 'Critical'],
        'count': [845, 287, 89, 26],
        'color': ['#28a745', '#ffc107', '#fd7e14', '#dc3545']
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
        # NPL Trend Chart
        npl_data = get_sample_npl_data()
        fig = px.line(npl_data, x='month', y='npl_ratio', 
                     title="📈 NPL Ratio Trend (12 Months)",
                     labels={'npl_ratio': 'NPL Ratio %', 'month': 'Month'})
        fig.update_traces(line=dict(color='#1f77b4', width=3))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk Distribution
        risk_data = get_sample_risk_distribution()
        fig = px.pie(risk_data, values='count', names='risk_band',
                    title="🎯 Risk Distribution Across Portfolio",
                    color='risk_band',
                    color_discrete_map={
                        'Low': '#28a745',
                        'Medium': '#ffc107', 
                        'High': '#fd7e14',
                        'Critical': '#dc3545'
                    })
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # At-Risk Loans Table
    st.subheader("🚨 Top At-Risk Loans Requiring Attention")
    
    at_risk_loans = get_sample_at_risk_loans()
    
    # Style the dataframe
    def style_risk_band(val):
        color_map = {
            'Critical': 'risk-critical',
            'High': 'risk-high',
            'Medium': 'risk-medium',
            'Low': 'risk-low'
        }
        return f'<span class="{color_map.get(val, "")}">{val}</span>'
    
    styled_df = at_risk_loans.copy()
    styled_df['Risk Band'] = styled_df['Risk Band'].apply(style_risk_band)
    
    st.markdown(styled_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
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
