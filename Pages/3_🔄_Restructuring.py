import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Restructuring - KCB SmartCredit",
    page_icon="🔄",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .proposal-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .affordability-good { color: #28a745; font-weight: bold; }
    .affordability-fair { color: #ffc107; font-weight: bold; }
    .affordability-poor { color: #dc3545; font-weight: bold; }
    .status-approved { background-color: #d4edda; color: #155724; padding: 0.25rem 0.5rem; border-radius: 4px; }
    .status-pending { background-color: #fff3cd; color: #856404; padding: 0.25rem 0.5rem; border-radius: 4px; }
    .status-completed { background-color: #d1ecf1; color: #0c5460; padding: 0.25rem 0.5rem; border-radius: 4px; }
    .status-rejected { background-color: #f8d7da; color: #721c24; padding: 0.25rem 0.5rem; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

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
    
    # Calculate affordability metrics
    disposable_income = borrower_income - monthly_expenses
    current_affordability_ratio = current_payment / disposable_income if disposable_income > 0 else 1
    
    st.write("### Affordability Assessment")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Disposable Income", f"KES {disposable_income:,}")
    with col_b:
        affordability_status = "Good" if current_affordability_ratio < 0.4 else "Fair" if current_affordability_ratio < 0.6 else "Poor"
        st.metric("Affordability", affordability_status)
    
    if st.button("Generate Restructuring Proposal", type="primary"):
        st.success("AI restructuring proposal generated!")
        
        # Calculate proposed payment (simplified logic)
        proposed_payment = current_payment * 0.62  # 38% reduction
        payment_reduction = ((current_payment - proposed_payment) / current_payment) * 100
        new_affordability_ratio = proposed_payment / disposable_income if disposable_income > 0 else 1
        affordability_improvement = ((current_affordability_ratio - new_affordability_ratio) / current_affordability_ratio) * 100
        
        # Display proposal in a nice card
        st.markdown('<div class="proposal-card">', unsafe_allow_html=True)
        st.subheader("📋 AI-Generated Restructuring Proposal")
        
        proposal_data = {
            "Current Payment": f"KES {current_payment:,}",
            "Proposed Payment": f"KES {proposed_payment:,.0f}",
            "Payment Reduction": f"{payment_reduction:.1f}%",
            "Term Extension": f"{term_extension} months",
            "Interest Rate Reduction": f"{interest_reduction:.1f}%",
            "Expected Recovery Rate": "82%",
            "Borrower Affordability Improvement": f"{affordability_improvement:.1f}%",
            "New Loan Term": f"{36 + term_extension} months total"
        }
        
        for key, value in proposal_data.items():
            col1, col2 = st.columns([2, 1])
            col1.write(f"**{key}:**")
            col2.write(value)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Action buttons for the proposal
        col_approve, col_modify, col_reject = st.columns(3)
        with col_approve:
            if st.button("✅ Approve Proposal", use_container_width=True):
                st.success("Proposal approved! Sending to borrower for acceptance.")
        with col_modify:
            if st.button("✏️ Modify Terms", use_container_width=True):
                st.info("Entering manual modification mode...")
        with col_reject:
            if st.button("❌ Reject Proposal", use_container_width=True):
                st.error("Proposal rejected. Please provide reasons.")

with col2:
    st.subheader("Affordability Analysis")
    
    # Cash flow analysis using native Streamlit
    st.write("**Monthly Cash Flow Analysis**")
    categories = ['Income', 'Current Payment', 'Proposed Payment', 'Living Expenses', 'Other Debt']
    amounts = [borrower_income, current_payment, current_payment * 0.62, monthly_expenses - 20000, 20000]
    
    cashflow_df = pd.DataFrame({
        'Category': categories,
        'Amount': amounts,
        'Type': ['Income', 'Expense', 'Expense', 'Expense', 'Expense']
    })
    
    # Display as bar chart using native Streamlit
    st.bar_chart(cashflow_df.set_index('Category')['Amount'])
    
    # Financial ratios
    st.write("**Financial Health Indicators**")
    
    ratio_col1, ratio_col2, ratio_col3 = st.columns(3)
    
    with ratio_col1:
        debt_ratio = (current_payment + 20000) / borrower_income * 100
        st.metric("Debt-to-Income Ratio", f"{debt_ratio:.1f}%")
    
    with ratio_col2:
        savings_ratio = (borrower_income - monthly_expenses - current_payment) / borrower_income * 100
        st.metric("Savings Rate", f"{max(0, savings_ratio):.1f}%")
    
    with ratio_col3:
        proposed_ratio = (current_payment * 0.62 + 20000) / borrower_income * 100
        st.metric("Proposed Debt Ratio", f"{proposed_ratio:.1f}%")
    
    # Payment comparison using native charts
    st.subheader("Payment Schedule Comparison")
    
    months = list(range(1, 13))
    current_balance = [450000 - i * current_payment for i in range(12)]
    proposed_payment_amount = current_payment * 0.62
    proposed_balance = [450000 - i * proposed_payment_amount for i in range(12)]
    
    comparison_df = pd.DataFrame({
        'Month': months * 2,
        'Balance': current_balance + proposed_balance,
        'Type': ['Current Plan'] * 12 + ['Proposed Plan'] * 12
    })
    
    # Use native line chart
    st.line_chart(comparison_df, x='Month', y='Balance', color='Type')

# Restructuring history with enhanced styling
st.subheader("📋 Recent Restructuring Activity")

restructuring_history = pd.DataFrame({
    'Loan ID': ['LN001', 'LN045', 'LN078', 'LN123', 'LN156'],
    'Borrower': ['John Doe', 'Mike Johnson', 'Sarah Wilson', 'David Brown', 'Alice Mwangi'],
    'Previous Payment': [45000, 38000, 52000, 28000, 32000],
    'New Payment': [28000, 25000, 35000, 20000, 22000],
    'Reduction %': [37.8, 34.2, 32.7, 28.6, 31.3],
    'Status': ['Approved', 'Pending', 'Completed', 'Rejected', 'Approved'],
    'Date': ['2024-01-15', '2024-01-14', '2024-01-10', '2024-01-08', '2024-01-05'],
    'Success Score': [85, 78, 92, 45, 88]
})

# Style the dataframe
def style_status(val):
    if val == 'Approved':
        return 'status-approved'
    elif val == 'Pending':
        return 'status-pending'
    elif val == 'Completed':
        return 'status-completed'
    else:
        return 'status-rejected'

# Display styled dataframe
styled_history = restructuring_history.copy()
styled_history['Status'] = styled_history['Status'].apply(style_status)

# Convert to HTML for styling
styled_html = styled_history.to_html(escape=False, index=False, classes='table table-striped')
st.markdown(styled_html, unsafe_allow_html=True)

# Restructuring statistics
st.subheader("📊 Restructuring Performance")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Success Rate", "76%", "+8%")

with stat_col2:
    st.metric("Avg. Payment Reduction", "32.9%", "+2.1%")

with stat_col3:
    st.metric("Recovery Improvement", "+18.5%", "+3.2%")

with stat_col4:
    st.metric("Processing Time", "3.2 days", "-0.8 days")

# Download options
st.subheader("📥 Export Options")

export_col1, export_col2, export_col3 = st.columns(3)

with export_col1:
    if st.button("📄 Generate Restructuring Report", use_container_width=True):
        st.success("Comprehensive restructuring report generated!")

with export_col2:
    csv_data = restructuring_history.to_csv(index=False)
    st.download_button(
        label="📊 Export as CSV",
        data=csv_data,
        file_name="restructuring_data.csv",
        mime="text/csv",
        use_container_width=True
    )

with export_col3:
    if st.button("📧 Send to Borrower", use_container_width=True):
        st.info("Restructuring proposal sent to borrower via email/SMS")

# Success stories
st.subheader("🎯 Success Stories")

success_stories = [
    {
        "case": "LN045 - Small Business",
        "result": "Payment reduced from KES 52,000 to KES 35,000",
        "impact": "Business continued operations, 3 jobs saved"
    },
    {
        "case": "LN078 - Family Mortgage", 
        "result": "Term extended by 18 months, interest reduced by 2%",
        "impact": "Family retained their home, continued payments"
    },
    {
        "case": "LN123 - Education Loan",
        "result": "Grace period of 6 months granted",
        "impact": "Student completed studies, now employed and repaying"
    }
]

for story in success_stories:
    with st.expander(f"✅ {story['case']}"):
        st.write(f"**Restructuring:** {story['result']}")
        st.write(f"**Impact:** {story['impact']}")
