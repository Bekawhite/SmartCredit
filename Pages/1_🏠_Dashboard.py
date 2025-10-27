import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.set_page_config(
    page_title="Dashboard - KCB SmartCredit",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Dashboard Overview")
st.markdown("Comprehensive view of your credit portfolio performance and key metrics")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Portfolio", "KES 245.7M", "2.1%")

with col2:
    st.metric("Active Loans", "1,247", "+18")

with col3:
    st.metric("Avg. Loan Size", "KES 197K", "-3.2%")

with col4:
    st.metric("Recovery Rate", "78.5%", "+5.2%")

# Charts
col1, col2 = st.columns(2)

with col1:
    # Portfolio growth
    months = pd.date_range('2023-01-01', periods=12, freq='M')
    portfolio_data = pd.DataFrame({
        'Month': months,
        'Portfolio Value (KES M)': [200, 210, 215, 220, 225, 230, 235, 238, 240, 242, 244, 245.7]
    })
    
    fig = px.line(portfolio_data, x='Month', y='Portfolio Value (KES M)',
                  title="Portfolio Growth Over Time")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Loan distribution by product
    product_data = pd.DataFrame({
        'Product': ['Personal Loans', 'Business Loans', 'Mortgages', 'Auto Loans', 'SME Credit'],
        'Count': [450, 320, 280, 150, 47],
        'Value (KES M)': [85.5, 98.2, 45.3, 12.5, 4.2]
    })
    
    fig = px.bar(product_data, x='Product', y='Count',
                 title="Loan Distribution by Product Type")
    st.plotly_chart(fig, use_container_width=True)

# Recent alerts
st.subheader("🔔 Recent Alerts & Notifications")

alerts = [
    {"type": "🚨", "message": "Loan LN001 - 45 days past due", "time": "2 hours ago"},
    {"type": "⚠️", "message": "Risk model retraining completed", "time": "5 hours ago"},
    {"type": "✅", "message": "Restructure approved for LN045", "time": "1 day ago"},
    {"type": "ℹ️", "message": "Monthly portfolio report generated", "time": "1 day ago"}
]

for alert in alerts:
    with st.container():
        col1, col2, col3 = st.columns([1, 8, 2])
        with col1:
            st.write(alert["type"])
        with col2:
            st.write(alert["message"])
        with col3:
            st.caption(alert["time"])
        st.divider()
