import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Dashboard - KCB SmartCredit",
    page_icon="🏠",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .alert-critical { border-left: 5px solid #dc3545; }
    .alert-warning { border-left: 5px solid #ffc107; }
    .alert-success { border-left: 5px solid #28a745; }
    .alert-info { border-left: 5px solid #17a2b8; }
</style>
""", unsafe_allow_html=True)

st.title("🏠 Dashboard Overview")
st.markdown("Comprehensive view of your credit portfolio performance and key metrics")

# KPI Metrics with enhanced styling
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total Portfolio", "KES 245.7M", "2.1%")
    st.caption("📈 +KES 5.1M this month")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Active Loans", "1,247", "+18")
    st.caption("🏦 89.3% performing")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Avg. Loan Size", "KES 197K", "-3.2%")
    st.caption("📊 Diversified portfolio")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Recovery Rate", "78.5%", "+5.2%")
    st.caption("🎯 Above target (75%)")
    st.markdown('</div>', unsafe_allow_html=True)

# Additional metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("NPL Ratio", "8.2%", "-1.2%", delta_color="inverse")

with col2:
    st.metric("Risk Score", "64.2", "-2.1")

with col3:
    st.metric("Restructured", "47", "+5")

with col4:
    st.metric("Collections", "KES 12.4M", "+1.2M")

# Charts using native Streamlit
st.subheader("📊 Portfolio Analytics")

col1, col2 = st.columns(2)

with col1:
    # Portfolio growth using native line chart
    st.write("**Portfolio Growth Over Time**")
    portfolio_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Portfolio Value (KES M)': [200, 210, 215, 220, 225, 230, 235, 238, 240, 242, 244, 245.7],
        'Target': [195, 205, 215, 225, 235, 240, 242, 243, 244, 245, 246, 247]
    })
    
    st.line_chart(
        portfolio_data,
        x='Month',
        y=['Portfolio Value (KES M)', 'Target'],
        color=['#1f77b4', '#ff7f0e']
    )

with col2:
    # Loan distribution by product
    st.write("**Loan Distribution by Product Type**")
    product_data = pd.DataFrame({
        'Product': ['Personal Loans', 'Business Loans', 'Mortgages', 'Auto Loans', 'SME Credit'],
        'Count': [450, 320, 280, 150, 47],
        'Value (KES M)': [85.5, 98.2, 45.3, 12.5, 4.2]
    })
    
    st.bar_chart(product_data, x='Product', y='Count')

# Performance metrics
st.subheader("🎯 Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Portfolio Health**")
    health_data = pd.DataFrame({
        'Status': ['Performing', 'Watch List', 'Restructured', 'NPL'],
        'Count': [1114, 89, 47, 102],
        'Percentage': [89.3, 7.1, 3.8, 8.2]
    })
    st.dataframe(health_data, use_container_width=True, hide_index=True)

with col2:
    st.write("**Top Performing Sectors**")
    sectors_data = pd.DataFrame({
        'Sector': ['Services', 'Manufacturing', 'Healthcare', 'Education', 'Retail'],
        'Growth': ['+12.5%', '+8.7%', '+15.2%', '+6.3%', '+4.1%'],
        'NPL Ratio': ['3.2%', '5.1%', '2.8%', '4.5%', '6.7%']
    })
    st.dataframe(sectors_data, use_container_width=True, hide_index=True)

with col3:
    st.write("**Regional Performance**")
    region_data = pd.DataFrame({
        'Region': ['Nairobi', 'Coast', 'Central', 'Rift Valley', 'Western'],
        'Portfolio (KES M)': [145.2, 38.7, 42.3, 15.8, 3.7],
        'Growth': ['+3.2%', '+1.8%', '+2.5%', '+4.1%', '+0.8%']
    })
    st.dataframe(region_data, use_container_width=True, hide_index=True)

# Recent alerts with enhanced styling
st.subheader("🔔 Recent Alerts & Notifications")

alerts = [
    {
        "type": "🚨 Critical", 
        "message": "Loan LN001 - 45 days past due - Requires immediate attention",
        "time": "2 hours ago",
        "priority": "alert-critical"
    },
    {
        "type": "⚠️ Warning", 
        "message": "Risk model retraining completed - New thresholds applied",
        "time": "5 hours ago", 
        "priority": "alert-warning"
    },
    {
        "type": "✅ Success", 
        "message": "Restructure approved for LN045 - Payment reduced by 35%",
        "time": "1 day ago",
        "priority": "alert-success"
    },
    {
        "type": "ℹ️ Info", 
        "message": "Monthly portfolio report generated - Ready for review",
        "time": "1 day ago",
        "priority": "alert-info"
    },
    {
        "type": "📊 Update", 
        "message": "12 new loan applications received - Awaiting review",
        "time": "2 days ago",
        "priority": "alert-info"
    }
]

for alert in alerts:
    with st.container():
        st.markdown(f'<div class="metric-card {alert["priority"]}">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2, 6, 2])
        with col1:
            st.write(f"**{alert['type']}**")
        with col2:
            st.write(alert["message"])
        with col3:
            st.caption(alert["time"])
        st.markdown('</div>', unsafe_allow_html=True)

# Quick actions
st.subheader("⚡ Quick Actions")

action_col1, action_col2, action_col3, action_col4 = st.columns(4)

with action_col1:
    if st.button("📋 Generate Report", use_container_width=True):
        st.success("Portfolio report generation started!")

with action_col2:
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.rerun()

with action_col3:
    if st.button("📧 Send Alerts", use_container_width=True):
        st.info("Alerts sent to relationship managers")

with action_col4:
    if st.button("🎯 Run Analysis", use_container_width=True):
        st.success("Risk analysis completed!")

# System status
st.subheader("🖥️ System Status")

status_col1, status_col2, status_col3, status_col4 = st.columns(4)

with status_col1:
    st.success("**API Status**\n\n✅ Operational")

with status_col2:
    st.info("**Data Freshness**\n\n🕒 2 hours ago")

with status_col3:
    st.warning("**Model Accuracy**\n\n📊 87.3%")

with status_col4:
    st.success("**Uptime**\n\n⏱️ 99.9%")

# Last updated
st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
