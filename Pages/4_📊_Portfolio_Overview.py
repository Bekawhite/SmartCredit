import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Portfolio Overview - KCB SmartCredit",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .portfolio-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .sector-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.25rem;
    }
    .metric-highlight {
        font-size: 1.2em;
        font-weight: bold;
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Portfolio Overview")
st.markdown("Comprehensive analysis of your loan portfolio performance")

# Portfolio metrics with enhanced styling
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="portfolio-card">', unsafe_allow_html=True)
    st.metric("Total Outstanding", "KES 245.7M", "2.1%")
    st.caption("📈 +KES 5.1M this month")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="portfolio-card">', unsafe_allow_html=True)
    st.metric("NPL Ratio", "8.2%", "-1.2%", delta_color="inverse")
    st.caption("🎯 Target: <7.5%")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="portfolio-card">', unsafe_allow_html=True)
    st.metric("Avg. Days Past Due", "14.2", "+0.8", delta_color="inverse")
    st.caption("📊 30+ DPD: 89 loans")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="portfolio-card">', unsafe_allow_html=True)
    st.metric("Recovery Rate", "78.5%", "+5.2%")
    st.caption("💪 Above industry average")
    st.markdown('</div>', unsafe_allow_html=True)

# Additional metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Portfolio Yield", "15.2%", "+0.3%")

with col2:
    st.metric("Cost of Risk", "1.8%", "-0.2%")

with col3:
    st.metric("Provision Coverage", "85.2%", "+3.5%")

with col4:
    st.metric("ROA", "2.8%", "+0.4%")

# Portfolio composition
st.subheader("🏗️ Portfolio Composition")

col1, col2 = st.columns(2)

with col1:
    # By sector - using native Streamlit
    st.write("**Portfolio Distribution by Sector**")
    sector_data = pd.DataFrame({
        'Sector': ['Agriculture', 'Manufacturing', 'Services', 'Retail', 'Tourism', 'Other'],
        'Value (KES M)': [45.0, 68.0, 55.7, 34.2, 23.8, 19.0],
        'Loans': [230, 320, 280, 180, 95, 142],
        'Growth': ['+2.1%', '+3.8%', '+1.5%', '-0.8%', '+5.2%', '+1.1%']
    })
    
    # Display as bar chart
    st.bar_chart(sector_data.set_index('Sector')['Value (KES M)'])
    
    # Show detailed table
    with st.expander("📋 View Sector Details"):
        st.dataframe(sector_data, use_container_width=True, hide_index=True)

with col2:
    # By product type - using native Streamlit
    st.write("**NPL Ratio by Product Type**")
    product_data = pd.DataFrame({
        'Product': ['Personal Loans', 'Business Loans', 'Mortgages', 'Auto Loans', 'SME Credit'],
        'NPL Ratio': [6.2, 9.8, 3.4, 5.1, 11.2],
        'Avg. Risk Score': [58, 72, 45, 52, 68],
        'Portfolio Share': ['34.8%', '40.0%', '18.4%', '5.1%', '1.7%']
    })
    
    # Display as bar chart
    st.bar_chart(product_data.set_index('Product')['NPL Ratio'])
    
    # Show detailed table
    with st.expander("📋 View Product Details"):
        st.dataframe(product_data, use_container_width=True, hide_index=True)

# Performance metrics
st.subheader("📈 Performance Metrics")

col1, col2 = st.columns(2)

with col1:
    # NPL trend by sector using native charts
    st.write("**NPL Ratio Trend by Sector**")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    trend_data = pd.DataFrame({
        'Month': months * 3,
        'NPL Ratio': 
            [8.5, 8.2, 7.9, 7.7, 7.8, 8.1, 8.4, 8.6, 8.3, 8.0, 7.8, 7.6] +  # Agriculture
            [9.2, 9.0, 8.8, 8.5, 8.7, 9.0, 9.3, 9.5, 9.2, 8.9, 8.7, 8.5] +  # Manufacturing
            [7.2, 7.0, 6.8, 6.5, 6.7, 7.0, 7.3, 7.5, 7.2, 6.9, 6.7, 6.5],   # Services
        'Sector': ['Agriculture'] * 12 + ['Manufacturing'] * 12 + ['Services'] * 12
    })
    
    # Use native line chart
    st.line_chart(trend_data, x='Month', y='NPL Ratio', color='Sector')

with col2:
    # Risk vs Return analysis using dataframe
    st.write("**Risk vs Return Analysis**")
    
    scatter_data = pd.DataFrame({
        'Product': ['Personal Loans', 'Business Loans', 'Mortgages', 'Auto Loans', 'SME Credit'],
        'Avg Interest Rate': [14.5, 16.2, 11.8, 13.5, 18.5],
        'NPL Ratio': [6.2, 9.8, 3.4, 5.1, 11.2],
        'Portfolio Size (KES M)': [85.5, 98.2, 45.3, 12.5, 4.2],
        'ROA': [3.2, 3.8, 2.1, 2.8, 4.5]
    })
    
    # Display as styled table
    def color_risk_return(row):
        if row['NPL Ratio'] < 5 and row['ROA'] > 3:
            return ['background-color: #d4edda'] * len(row)
        elif row['NPL Ratio'] > 10:
            return ['background-color: #f8d7da'] * len(row)
        else:
            return ['background-color: #fff3cd'] * len(row)
    
    st.dataframe(
        scatter_data.style.apply(color_risk_return, axis=1),
        use_container_width=True,
        hide_index=True
    )

# Portfolio quality indicators
st.subheader("🎯 Portfolio Quality Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Credit Quality Distribution**")
    quality_data = pd.DataFrame({
        'Rating': ['A (Excellent)', 'B (Good)', 'C (Fair)', 'D (Watch)', 'E (Substandard)'],
        'Loans': [445, 387, 215, 89, 111],
        'Percentage': ['35.7%', '31.0%', '17.2%', '7.1%', '8.9%']
    })
    st.dataframe(quality_data, use_container_width=True, hide_index=True)

with col2:
    st.write("**Geographic Distribution**")
    geo_data = pd.DataFrame({
        'Region': ['Nairobi', 'Central', 'Coast', 'Rift Valley', 'Western', 'Eastern'],
        'Portfolio (KES M)': [145.2, 38.7, 28.4, 15.8, 12.3, 5.3],
        'Growth': ['+3.2%', '+1.8%', '+2.1%', '+4.1%', '+0.8%', '+1.2%']
    })
    st.dataframe(geo_data, use_container_width=True, hide_index=True)

with col3:
    st.write("**Loan Size Distribution**")
    size_data = pd.DataFrame({
        'Range': ['< 100K', '100K-500K', '500K-1M', '1M-5M', '> 5M'],
        'Loans': [567, 432, 158, 76, 14],
        'Value (KES M)': [28.4, 86.5, 105.3, 152.8, 12.7]
    })
    st.dataframe(size_data, use_container_width=True, hide_index=True)

# Portfolio statistics table
st.subheader("📋 Detailed Portfolio Statistics")

portfolio_stats = pd.DataFrame({
    'Metric': [
        'Total Number of Loans',
        'Average Loan Size',
        'Weighted Average Interest Rate',
        'Portfolio Duration',
        'Concentration Ratio (Top 10%)',
        'Provision Coverage Ratio',
        'Cost of Risk',
        'Return on Risk Assets',
        'Capital Adequacy Ratio',
        'Liquidity Coverage Ratio'
    ],
    'Value': [
        '1,247',
        'KES 197,000',
        '14.8%',
        '2.8 years',
        '28.5%',
        '85.2%',
        '1.8%',
        '3.2%',
        '18.5%',
        '125.3%'
    ],
    'Change': [
        '+18',
        '-3.2%',
        '+0.2%',
        '+0.1 years',
        '-2.1%',
        '+3.5%',
        '-0.3%',
        '+0.4%',
        '+0.8%',
        '+5.2%'
    ],
    'Status': [
        '✅ Good', '✅ Good', '✅ Good', '✅ Good', '⚠️ Watch',
        '✅ Good', '✅ Good', '✅ Good', '✅ Good', '✅ Excellent'
    ]
})

# Style the dataframe
def style_status(val):
    if 'Excellent' in val:
        return 'color: #28a745; font-weight: bold;'
    elif 'Good' in val:
        return 'color: #20c997; font-weight: bold;'
    elif 'Watch' in val:
        return 'color: #ffc107; font-weight: bold;'
    else:
        return 'color: #dc3545; font-weight: bold;'

st.dataframe(
    portfolio_stats.style.applymap(style_status, subset=['Status']),
    use_container_width=True,
    hide_index=True
)

# Portfolio actions and insights
st.subheader("💡 Portfolio Insights & Actions")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.info("""
    **🎯 Strengths:**
    - Strong recovery rate improvement (+5.2%)
    - Diversified sector exposure
    - Healthy provision coverage
    - Stable portfolio growth
    """)

with insight_col2:
    st.warning("""
    **⚠️ Areas for Improvement:**
    - Monitor SME credit segment (11.2% NPL)
    - Address increasing DPD in manufacturing
    - Review concentration in top 10% loans
    - Enhance tourism sector monitoring
    """)

# Quick actions
st.subheader("⚡ Quick Actions")

action_col1, action_col2, action_col3, action_col4 = st.columns(4)

with action_col1:
    if st.button("📄 Generate Report", use_container_width=True):
        st.success("Portfolio analysis report generated!")

with action_col2:
    if st.button("🔄 Run Stress Test", use_container_width=True):
        st.info("Stress testing in progress...")

with action_col3:
    if st.button("📊 Update Models", use_container_width=True):
        st.success("Risk models updated successfully!")

with action_col4:
    if st.button("📧 Share Insights", use_container_width=True):
        st.info("Portfolio insights shared with management")

# Last updated
st.markdown("---")
st.caption(f"📅 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Data source: Core Banking System")
