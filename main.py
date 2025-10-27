import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="KCB SmartCredit",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
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
    .nav-button {
        width: 100%;
        margin: 0.25rem 0;
        padding: 0.75rem;
        border: none;
        border-radius: 8px;
        background: #f8f9fa;
        color: #2c3e50;
        font-size: 1rem;
        text-align: left;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .nav-button:hover {
        background: #1f77b4;
        color: white;
        transform: translateX(5px);
    }
    .nav-button.active {
        background: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .section-header {
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard"

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

# Page functions
def dashboard_page():
    st.markdown('<div class="main-header">🏦 KCB SmartCredit - Credit Risk Management Platform</div>', unsafe_allow_html=True)
    
    # Quick stats row
    st.markdown('<div class="section-header">📈 Portfolio Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="NPL Ratio",
            value="8.2%",
            delta="-1.2%",
            delta_color="inverse"
        )
        st.caption("📊 102 non-performing loans")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Total Portfolio",
            value="KES 245.7M",
            delta="+2.1%"
        )
        st.caption("🏦 1,247 active loans")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Avg. Risk Score",
            value="62.3",
            delta="-4.1"
        )
        st.caption("📈 Improving trend")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            label="Recovery Rate",
            value="78.5%",
            delta="+5.2%"
        )
        st.caption("🎯 Above target (75%)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Charts Section
    st.markdown('<div class="section-header">📊 Portfolio Analytics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**📈 NPL Ratio Trend (12 Months)**")
        npl_data = get_sample_npl_data()
        st.line_chart(npl_data, x='month', y='npl_ratio', height=350)
    
    with col2:
        st.write("**🎯 Risk Distribution Across Portfolio**")
        risk_data = get_sample_risk_distribution()
        st.bar_chart(risk_data.set_index('risk_band')['count'], height=350)
    
    # At-Risk Loans Table
    st.markdown('<div class="section-header">🚨 High Priority Actions</div>', unsafe_allow_html=True)
    
    at_risk_loans = get_sample_at_risk_loans()
    st.dataframe(at_risk_loans, use_container_width=True)
    
    # Recent Activity
    st.markdown('<div class="section-header">🕒 Recent Activity</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**📈 Last Risk Model Update**\n\n2 hours ago")
    
    with col2:
        st.success("**🔄 Successful Restructures**\n\n12 this week")
    
    with col3:
        st.warning("**⏳ Pending Approvals**\n\n8 requests")

def risk_analysis_page():
    st.title("🔍 Risk Analysis")
    st.markdown("Deep dive into borrower risk profiles and portfolio risk metrics")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Individual Risk Assessment")
        
        borrower_id = st.selectbox(
            "Select Borrower",
            ["BORR001 - John Doe", "BORR002 - Jane Smith", "BORR003 - Mike Johnson"]
        )
        
        monthly_income = st.number_input("Monthly Income (KES)", value=150000, step=10000)
        existing_debt = st.number_input("Existing Debt (KES)", value=450000, step=10000)
        loan_amount = st.number_input("Loan Amount Requested (KES)", value=200000, step=10000)
        employment_type = st.selectbox("Employment Type", ["Salaried", "Business Owner", "Self-Employed"])
        credit_history = st.slider("Credit History (Months)", 0, 120, 36)
        
        if st.button("Assess Risk", type="primary"):
            st.success("Risk assessment completed!")
            
            # Calculate risk score
            debt_to_income = (existing_debt + loan_amount) / (monthly_income * 12) * 100
            risk_score = min(100, max(20, debt_to_income + (120 - credit_history) * 0.5))
            
            st.metric("Risk Score", f"{risk_score:.1f}/100")
            
            # Risk factors
            st.subheader("Key Risk Factors")
            risk_factors = []
            
            if debt_to_income > 50:
                risk_factors.append(f"High debt-to-income ratio ({debt_to_income:.1f}%)")
            if credit_history < 24:
                risk_factors.append("Limited credit history")
            if employment_type == "Self-Employed":
                risk_factors.append("Variable income source")
                
            for factor in risk_factors:
                st.write(f"• {factor}")
    
    with col2:
        st.subheader("Portfolio Risk Overview")
        
        # Risk distribution
        risk_data = get_sample_risk_distribution()
        st.bar_chart(risk_data.set_index('risk_band')['count'], height=300)
        
        # Risk metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Overall Risk Score", "64.2", "+2.1")
        with col2:
            st.metric("High Risk Loans", "89", "+8", delta_color="inverse")
        with col3:
            st.metric("Risk Concentration", "28%", "-3%")

def restructuring_page():
    st.title("🔄 Loan Restructuring")
    st.markdown("AI-powered restructuring proposals and affordability analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Restructuring Proposal Generator")
        
        loan_id = st.selectbox(
            "Select Loan for Restructuring",
            ["LN001 - John Doe (45 DPD)", "LN002 - Jane Smith (32 DPD)", "LN045 - Mike Johnson (28 DPD)"]
        )
        
        current_payment = st.number_input("Current Monthly Payment (KES)", value=45000, step=1000)
        borrower_income = st.number_input("Borrower Monthly Income (KES)", value=120000, step=5000)
        monthly_expenses = st.number_input("Total Monthly Expenses (KES)", value=95000, step=5000)
        term_extension = st.slider("Proposed Term Extension (Months)", 0, 24, 12)
        interest_reduction = st.slider("Interest Rate Reduction (%)", 0.0, 5.0, 1.5, step=0.1)
        
        if st.button("Generate Restructuring Proposal", type="primary"):
            st.success("AI restructuring proposal generated!")
            
            # Calculate proposal
            proposed_payment = current_payment * 0.62
            payment_reduction = ((current_payment - proposed_payment) / current_payment) * 100
            
            proposal = {
                "Current Payment": f"KES {current_payment:,}",
                "Proposed Payment": f"KES {proposed_payment:,.0f}",
                "Payment Reduction": f"{payment_reduction:.1f}%",
                "Term Extension": f"{term_extension} months",
                "Interest Rate Reduction": f"{interest_reduction:.1f}%",
                "Expected Recovery Rate": "82%"
            }
            
            for key, value in proposal.items():
                col1, col2 = st.columns([2, 1])
                col1.write(f"**{key}:**")
                col2.write(value)
    
    with col2:
        st.subheader("Affordability Analysis")
        
        # Cash flow chart
        categories = ['Income', 'Current Payment', 'Proposed Payment', 'Living Expenses', 'Other Debt']
        amounts = [borrower_income, current_payment, current_payment * 0.62, monthly_expenses - 20000, 20000]
        
        cashflow_df = pd.DataFrame({
            'Category': categories,
            'Amount': amounts
        })
        
        st.bar_chart(cashflow_df.set_index('Category')['Amount'], height=300)
        
        # Financial ratios
        st.subheader("Financial Health Indicators")
        
        ratio_col1, ratio_col2 = st.columns(2)
        with ratio_col1:
            debt_ratio = (current_payment + 20000) / borrower_income * 100
            st.metric("Debt-to-Income Ratio", f"{debt_ratio:.1f}%")
        with ratio_col2:
            proposed_ratio = (current_payment * 0.62 + 20000) / borrower_income * 100
            st.metric("Proposed Debt Ratio", f"{proposed_ratio:.1f}%")

def portfolio_page():
    st.title("📊 Portfolio Overview")
    st.markdown("Comprehensive analysis of your loan portfolio performance")
    
    # Portfolio metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Outstanding", "KES 245.7M", "2.1%")
    
    with col2:
        st.metric("NPL Ratio", "8.2%", "-1.2%", delta_color="inverse")
    
    with col3:
        st.metric("Avg. Days Past Due", "14.2", "+0.8", delta_color="inverse")
    
    with col4:
        st.metric("Recovery Rate", "78.5%", "+5.2%")
    
    # Portfolio composition
    st.subheader("Portfolio Composition")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**By Sector**")
        sector_data = pd.DataFrame({
            'Sector': ['Agriculture', 'Manufacturing', 'Services', 'Retail', 'Tourism', 'Other'],
            'Value (KES M)': [45.0, 68.0, 55.7, 34.2, 23.8, 19.0]
        })
        st.bar_chart(sector_data.set_index('Sector')['Value (KES M)'])
    
    with col2:
        st.write("**By Product Type**")
        product_data = pd.DataFrame({
            'Product': ['Personal Loans', 'Business Loans', 'Mortgages', 'Auto Loans', 'SME Credit'],
            'NPL Ratio': [6.2, 9.8, 3.4, 5.1, 11.2]
        })
        st.bar_chart(product_data.set_index('Product')['NPL Ratio'])
    
    # Performance metrics
    st.subheader("Performance Metrics")
    
    # NPL trend
    npl_data = get_sample_npl_data()
    st.line_chart(npl_data, x='month', y='npl_ratio', height=300)
    
    # Portfolio statistics
    st.subheader("Portfolio Statistics")
    
    portfolio_stats = pd.DataFrame({
        'Metric': ['Total Loans', 'Average Loan Size', 'Interest Rate', 'Portfolio Duration'],
        'Value': ['1,247', 'KES 197,000', '14.8%', '2.8 years'],
        'Change': ['+18', '-3.2%', '+0.2%', '+0.1 years']
    })
    
    st.dataframe(portfolio_stats, use_container_width=True, hide_index=True)

def admin_page():
    st.title("⚙️ Admin Panel")
    st.markdown("System configuration and management")
    
    tab1, tab2, tab3 = st.tabs(["Model Management", "System Monitoring", "Configuration"])
    
    with tab1:
        st.subheader("ML Model Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.selectbox("Active Risk Model Version", ["v2.1.0 (Production)", "v2.0.0", "v1.5.0"])
            st.selectbox("NPL Forecast Model", ["v1.2.0 (Production)", "v1.1.0"])
            st.number_input("Retraining Frequency (Days)", value=30, min_value=1, max_value=90)
            
            if st.button("Schedule Model Retraining", type="primary"):
                st.success("Model retraining scheduled!")
        
        with col2:
            st.subheader("Model Performance")
            
            performance_data = pd.DataFrame({
                'Model': ['Risk Assessment', 'NPL Forecast', 'Restructuring'],
                'Accuracy': [87.3, 92.1, 78.5],
                'Last Updated': ['2 hours ago', '1 day ago', '3 days ago']
            })
            
            st.dataframe(performance_data, use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("System Health Monitoring")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("API Response Time", "142ms", "-8ms")
        
        with col2:
            st.metric("Database Connections", "24/50", "+2")
        
        with col3:
            st.metric("Active Users", "17", "+3")
        
        with col4:
            st.metric("Error Rate", "0.2%", "-0.1%")
    
    with tab3:
        st.subheader("System Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.number_input("Risk Score Threshold - Critical", value=80)
            st.number_input("Risk Score Threshold - High", value=60)
            st.number_input("NPL Alert Threshold (%)", value=10.0)
        
        with col2:
            st.number_input("Max Restructuring Term (Months)", value=60)
            st.number_input("Auto-approval Limit (KES)", value=50000)
        
        if st.button("Save Configuration", type="primary"):
            st.success("Configuration saved successfully!")

# Navigation sidebar
def navigation_sidebar():
    st.sidebar.image("https://via.placeholder.com/150x50/1f77b4/ffffff?text=KCB", width=150)
    st.sidebar.title("Navigation")
    
    # Navigation buttons
    pages = {
        "🏠 Dashboard": dashboard_page,
        "🔍 Risk Analysis": risk_analysis_page,
        "🔄 Restructuring": restructuring_page,
        "📊 Portfolio Overview": portfolio_page,
        "⚙️ Admin": admin_page
    }
    
    for page_name, page_function in pages.items():
        is_active = st.session_state.current_page == page_name
        button_class = "nav-button active" if is_active else "nav-button"
        
        if st.sidebar.button(page_name, key=page_name, use_container_width=True):
            st.session_state.current_page = page_name
            st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.info("**System Status**\n\n✅ All systems operational\n🕒 Last updated: 2 min ago")

# Main app function
def main():
    # Render navigation
    navigation_sidebar()
    
    # Render current page
    pages = {
        "🏠 Dashboard": dashboard_page,
        "🔍 Risk Analysis": risk_analysis_page,
        "🔄 Restructuring": restructuring_page,
        "📊 Portfolio Overview": portfolio_page,
        "⚙️ Admin": admin_page
    }
    
    # Call the current page function
    current_page_function = pages.get(st.session_state.current_page, dashboard_page)
    current_page_function()

if __name__ == "__main__":
    main()
