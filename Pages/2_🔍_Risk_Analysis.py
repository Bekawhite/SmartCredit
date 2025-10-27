import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Risk Analysis - KCB SmartCredit",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Risk Analysis")
st.markdown("Deep dive into borrower risk profiles and portfolio risk metrics")

# Risk assessment input
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
        
        # Calculate risk score based on inputs
        debt_to_income = (existing_debt + loan_amount) / (monthly_income * 12) * 100
        risk_score = min(100, max(20, debt_to_income + (120 - credit_history) * 0.5))
        
        # Determine risk band
        if risk_score >= 80:
            risk_band = "Critical"
            risk_color = "red"
        elif risk_score >= 60:
            risk_band = "High"
            risk_color = "orange"
        elif risk_score >= 40:
            risk_band = "Medium" 
            risk_color = "yellow"
        else:
            risk_band = "Low"
            risk_color = "green"
        
        st.metric("Risk Score", f"{risk_score:.1f}/100")
        st.markdown(f"**Risk Band:** :{risk_color}[{risk_band} Risk]")
        
        # Risk factors
        st.subheader("Key Risk Factors")
        risk_factors = []
        
        if debt_to_income > 50:
            risk_factors.append(f"High debt-to-income ratio ({debt_to_income:.1f}%)")
        if credit_history < 24:
            risk_factors.append("Limited credit history")
        if employment_type == "Self-Employed":
            risk_factors.append("Variable income source")
        if monthly_income < 100000:
            risk_factors.append("Low income level")
        if loan_amount > monthly_income * 6:
            risk_factors.append("High loan-to-income ratio")
            
        if not risk_factors:
            risk_factors.append("No major risk factors identified")
            
        for factor in risk_factors:
            st.write(f"• {factor}")

with col2:
    st.subheader("Portfolio Risk Heatmap")
    
    # Generate sample heatmap data
    sectors = ['Agriculture', 'Manufacturing', 'Services', 'Retail', 'Tourism']
    risk_bands = ['Low', 'Medium', 'High', 'Critical']
    
    # Create a matrix for the heatmap
    heatmap_data = []
    for i, sector in enumerate(sectors):
        row_data = {'Sector': sector}
        for j, band in enumerate(risk_bands):
            # Create a pattern where risk increases diagonally
            count = max(5, 50 - (i * 10) - (j * 8) + np.random.randint(-5, 5))
            row_data[band] = count
        heatmap_data.append(row_data)
    
    heatmap_df = pd.DataFrame(heatmap_data)
    
    # Display as a styled dataframe (heatmap alternative)
    st.write("**Risk Distribution by Sector**")
    
    def color_risk_cells(val):
        if val > 40:
            return 'background-color: #d4edda'  # Green for low risk
        elif val > 25:
            return 'background-color: #fff3cd'  # Yellow for medium risk
        elif val > 15:
            return 'background-color: #ffeaa7'  # Orange for high risk
        else:
            return 'background-color: #f8d7da'  # Red for critical
    
    display_df = heatmap_df.set_index('Sector')
    st.dataframe(display_df.style.applymap(color_risk_cells), use_container_width=True)
    
    # Risk over time - using native Streamlit charts
    st.subheader("Risk Trend Analysis")
    
    trend_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Avg Risk Score': [58, 59, 61, 63, 65, 64, 66, 67, 65, 63, 62, 61],
        'High Risk %': [12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15]
    })
    
    # Create two columns for the charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.write("**Average Risk Score Over Time**")
        st.line_chart(trend_data, x='Month', y='Avg Risk Score')
    
    with chart_col2:
        st.write("**High Risk Percentage Over Time**")
        st.line_chart(trend_data, x='Month', y='High Risk %')

# Additional risk metrics
st.subheader("📊 Portfolio Risk Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Overall Risk Score", "64.2", "+2.1")

with col2:
    st.metric("High Risk Loans", "89", "+8", delta_color="inverse")

with col3:
    st.metric("Risk Concentration", "28%", "-3%")

with col4:
    st.metric("Early Warning Signals", "12", "+2", delta_color="inverse")

# Risk mitigation recommendations
st.subheader("🎯 Risk Mitigation Recommendations")

recommendations = [
    {
        "priority": "High",
        "action": "Increase collateral requirements for SME sector",
        "impact": "Reduce potential losses by 15%",
        "timeline": "Immediate"
    },
    {
        "priority": "Medium", 
        "action": "Implement stricter debt-to-income checks",
        "impact": "Improve portfolio quality",
        "timeline": "30 days"
    },
    {
        "priority": "Low",
        "action": "Enhance credit monitoring for retail segment",
        "impact": "Early detection of defaults",
        "timeline": "60 days"
    }
]

for rec in recommendations:
    with st.expander(f"{rec['priority']} Priority: {rec['action']}"):
        st.write(f"**Expected Impact:** {rec['impact']}")
        st.write(f"**Implementation Timeline:** {rec['timeline']}")
        if st.button(f"Implement {rec['priority']} Priority Action", key=rec['action']):
            st.success(f"Action initiated: {rec['action']}")

# Download risk report
st.subheader("📥 Reports")

if st.button("Generate Risk Analysis Report"):
    with st.spinner("Generating comprehensive risk report..."):
        # Simulate report generation
        import time
        time.sleep(2)
        
        # Create sample report data
        report_data = {
            'Report Type': 'Comprehensive Risk Analysis',
            'Generated On': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Portfolio Size': '1,247 loans',
            'Total Exposure': 'KES 245.7M',
            'Overall Risk Rating': 'Moderate',
            'Key Findings': [
                'SME sector showing increased risk',
                'Tourism sector requires monitoring',
                'Overall portfolio quality stable'
            ]
        }
        
        st.success("Risk report generated successfully!")
        st.json(report_data)
        
        # Provide download option
        csv_data = heatmap_df.to_csv(index=False)
        st.download_button(
            label="Download Risk Data as CSV",
            data=csv_data,
            file_name="risk_analysis_data.csv",
            mime="text/csv"
        )
