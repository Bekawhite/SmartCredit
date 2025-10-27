import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utils.helpers import (
    generate_sample_borrowers,
    generate_sample_loans,
    format_currency,
    calculate_risk_band,
    get_risk_color,
    generate_portfolio_summary,
    create_sample_npl_trend
)

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
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #1f77b4;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .risk-critical { 
        color: #dc3545; 
        font-weight: bold;
        background-color: #f8d7da;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
    }
    .risk-high { 
        color: #fd7e14; 
        font-weight: bold;
        background-color: #ffeaa7;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
    }
    .risk-medium { 
        color: #ffc107; 
        font-weight: bold;
        background-color: #fff3cd;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
    }
    .risk-low { 
        color: #28a745; 
        font-weight: bold;
        background-color: #d4edda;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
    }
    .section-header {
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        color: #2c3e50;
    }
    .alert-badge {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 0.25rem;
    }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Initialize session state for sample data
if 'sample_data_loaded' not in st.session_state:
    st.session_state.sample_data_loaded = False
    st.session_state.borrowers_df = generate_sample_borrowers(150)
    st.session_state.loans_df = generate_sample_loans(300)
    st.session_state.sample_data_loaded = True

# Sample data functions using generated data
def get_sample_npl_data():
    """Get NPL trend data"""
    return create_sample_npl_trend()

def get_sample_risk_distribution():
    """Get risk distribution from sample data"""
    risk_counts = st.session_state.loans_df['risk_band'].value_counts()
    return pd.DataFrame({
        'risk_band': risk_counts.index,
        'count': risk_counts.values
    })

def get_sample_at_risk_loans():
    """Get top at-risk loans from sample data"""
    high_risk_loans = st.session_state.loans_df[
        st.session_state.loans_df['risk_band'].isin(['High', 'Critical'])
    ].nlargest(8, 'outstanding_balance')
    
    return pd.DataFrame({
        'Loan ID': high_risk_loans['loan_id'].values,
        'Borrower': [f"Borrower {i}" for i in range(len(high_risk_loans))],
        'Risk Score': np.random.randint(70, 96, len(high_risk_loans)),
        'Outstanding (KES)': high_risk_loans['outstanding_balance'].values,
        'Days Past Due': high_risk_loans['days_past_due'].values,
        'Risk Band': high_risk_loans['risk_band'].values,
        'Product Type': high_risk_loans['product_type'].values
    })

def get_portfolio_metrics():
    """Calculate comprehensive portfolio metrics"""
    portfolio_stats = generate_portfolio_summary(st.session_state.loans_df)
    
    return {
        "total_loans": portfolio_stats["total_loans"],
        "total_outstanding": portfolio_stats["total_outstanding"],
        "npl_ratio": portfolio_stats["npl_ratio"],
        "npl_count": portfolio_stats["npl_count"],
        "avg_loan_size": portfolio_stats["average_loan_size"],
        "recovery_rate": 78.5,  # Sample data
        "avg_risk_score": 62.3  # Sample data
    }

def main():
    # Main header
    st.markdown('<div class="main-header">🏦 KCB SmartCredit - Credit Risk Management Platform</div>', unsafe_allow_html=True)
    
    # Portfolio metrics
    portfolio_metrics = get_portfolio_metrics()
    
    # Quick stats row
    st.markdown('<div class="section-header">📈 Portfolio Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="NPL Ratio",
            value=f"{portfolio_metrics['npl_ratio']:.1f}%",
            delta="-1.2%",
            delta_color="inverse"
        )
        st.caption(f"📊 {portfolio_metrics['npl_count']} non-performing loans")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Total Portfolio",
            value=format_currency(portfolio_metrics['total_outstanding']),
            delta="+2.1%"
        )
        st.caption(f"🏦 {portfolio_metrics['total_loans']} active loans")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Avg. Risk Score",
            value=f"{portfolio_metrics['avg_risk_score']:.1f}",
            delta="-4.1"
        )
        st.caption("📈 Improving trend")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Recovery Rate",
            value=f"{portfolio_metrics['recovery_rate']:.1f}%",
            delta="+5.2%"
        )
        st.caption("🎯 Above target (75%)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Avg. Loan Size", format_currency(portfolio_metrics['avg_loan_size']), "-3.2%")
    
    with col2:
        st.metric("High Risk Loans", "47", "+3", delta_color="inverse")
    
    with col3:
        st.metric("Restructured", "23", "+5")
    
    with col4:
        st.metric("Collections", "KES 12.4M", "+1.2M")
    
    # Charts Section
    st.markdown('<div class="section-header">📊 Portfolio Analytics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # NPL Trend Chart
        st.write("**📈 NPL Ratio Trend (12 Months)**")
        npl_data = get_sample_npl_data()
        st.line_chart(npl_data, x='month', y='npl_ratio', height=350)
        
        # Additional NPL insights
        with st.expander("📋 NPL Analysis Details"):
            st.write(f"**Current NPL Ratio:** {npl_data['npl_ratio'].iloc[-1]:.1f}%")
            st.write(f"**Trend:** {'Improving' if npl_data['npl_ratio'].iloc[-1] < npl_data['npl_ratio'].iloc[0] else 'Deteriorating'}")
            st.write(f"**Volatility:** {npl_data['npl_ratio'].std():.2f}%")
    
    with col2:
        # Risk Distribution
        st.write("**🎯 Risk Distribution Across Portfolio**")
        risk_data = get_sample_risk_distribution()
        
        # Create a bar chart
        st.bar_chart(risk_data.set_index('risk_band')['count'], height=350)
        
        # Risk distribution insights
        with st.expander("📋 Risk Analysis Details"):
            total_loans = risk_data['count'].sum()
            for _, row in risk_data.iterrows():
                percentage = (row['count'] / total_loans) * 100
                risk_class = row['risk_band'].lower()
                st.write(f"**{row['risk_band']} Risk:** {row['count']} loans ({percentage:.1f}%)")
    
    # At-Risk Loans Section
    st.markdown('<div class="section-header">🚨 High Priority Actions</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Top At-Risk Loans Requiring Attention")
        at_risk_loans = get_sample_at_risk_loans()
        
        # Style the risk bands in the dataframe
        def style_risk_band(val):
            color_class = f"risk-{val.lower()}"
            return f'<span class="{color_class}">{val}</span>'
        
        styled_df = at_risk_loans.copy()
        styled_df['Outstanding (KES)'] = styled_df['Outstanding (KES)'].apply(
            lambda x: format_currency(x)
        )
        
        # Convert to HTML for styling
        styled_html = styled_df.to_html(escape=False, index=False, classes='table table-striped')
        st.markdown(styled_html, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🔄 Quick Actions")
        
        action_col1, action_col2 = st.columns(2)
        
        with action_col1:
            if st.button("📋 Generate Report", use_container_width=True):
                st.success("Portfolio report generated!")
            
            if st.button("🔍 Risk Analysis", use_container_width=True):
                st.info("Running comprehensive risk analysis...")
        
        with action_col2:
            if st.button("🔄 Refresh Data", use_container_width=True):
                st.rerun()
            
            if st.button("📧 Send Alerts", use_container_width=True):
                st.info("Alerts sent to relationship managers")
        
        # Priority alerts
        st.subheader("📢 Priority Alerts")
        st.markdown('<div class="alert-badge">🚨 3 Critical Risk Loans</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-badge">⚠️ 12 Restructuring Pending</div>', unsafe_allow_html=True)
        st.markdown('<div class="alert-badge">📊 Model Retraining Due</div>', unsafe_allow_html=True)
    
    # Recent Activity & System Status
    st.markdown('<div class="section-header">🕒 Recent Activity & System Status</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **📈 Last Risk Model Update**  
        🕒 2 hours ago  
        ✅ Accuracy: 87.3%  
        🔄 Next retraining: 3 days
        """)
    
    with col2:
        st.success("""
        **🔄 Successful Restructures**  
        📊 12 completed this week  
        💰 Total value: KES 4.2M  
        🎯 Success rate: 82%
        """)
    
    with col3:
        st.warning("""
        **⏳ Pending Approvals**  
        📝 8 restructuring requests  
        🏦 3 new loan applications  
        ⚠️ 2 credit limit increases
        """)
    
    # System Health Status
    st.markdown("---")
    health_col1, health_col2, health_col3, health_col4 = st.columns(4)
    
    with health_col1:
        st.success("**API Status**\n\n✅ Operational")
    
    with health_col2:
        st.info("**Data Freshness**\n\n🕒 15 minutes ago")
    
    with health_col3:
        st.warning("**System Load**\n\n📊 45% capacity")
    
    with health_col4:
        st.success("**Uptime**\n\n⏱️ 99.9% this month")
    
    # Footer
    st.markdown("---")
    footer_col1, footer_col2, footer_col3 = st.columns(3)
    with footer_col1:
        st.caption(f"🕒 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    with footer_col2:
        st.caption("🏦 KCB SmartCredit v2.1.0")
    with footer_col3:
        st.caption("🔐 Secure Banking Platform")

# Refresh data function
def refresh_sample_data():
    """Refresh sample data in session state"""
    st.session_state.borrowers_df = generate_sample_borrowers(150)
    st.session_state.loans_df = generate_sample_loans(300)
    st.success("Sample data refreshed!")

if __name__ == "__main__":
    main()
    
    # Debug button (hidden in production)
    with st.sidebar:
        if st.button("🔄 Debug: Refresh Sample Data", key="debug_refresh"):
            refresh_sample_data()
