import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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
    
    st.number_input("Monthly Income (KES)", value=150000, step=10000)
    st.number_input("Existing Debt (KES)", value=450000, step=10000)
    st.number_input("Loan Amount Requested (KES)", value=200000, step=10000)
    st.selectbox("Employment Type", ["Salaried", "Business Owner", "Self-Employed"])
    st.slider("Credit History (Months)", 0, 120, 36)
    
    if st.button("Assess Risk", type="primary"):
        st.success("Risk assessment completed!")
        
        # Display results
        risk_score = 72
        risk_band = "High Risk"
        
        st.metric("Risk Score", f"{risk_score}/100")
        
        # Risk factors
        st.subheader("Key Risk Factors")
        risk_factors = [
            "High debt-to-income ratio (65%)",
            "Recent payment delays (2 instances)",
            "Limited credit history",
            "Single source of income"
        ]
        
        for factor in risk_factors:
            st.write(f"• {factor}")

with col2:
    st.subheader("Portfolio Risk Heatmap")
    
    # Generate sample heatmap data
    sectors = ['Agriculture', 'Manufacturing', 'Services', 'Retail', 'Tourism']
    risk_bands = ['Low', 'Medium', 'High', 'Critical']
    
    heatmap_data = []
    for sector in sectors:
        for band in risk_bands:
            heatmap_data.append({
                'Sector': sector,
                'Risk Band': band,
                'Count': np.random.randint(5, 50)
            })
    
    heatmap_df = pd.DataFrame(heatmap_data)
    
    fig = px.density_heatmap(heatmap_df, x='Sector', y='Risk Band', z='Count',
                            title="Risk Distribution by Sector",
                            color_continuous_scale="RdYlGn_r")
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk over time
    st.subheader("Risk Trend Analysis")
    
    trend_data = pd.DataFrame({
        'Month': pd.date_range('2023-01-01', periods=12, freq='M'),
        'Avg Risk Score': [58, 59, 61, 63, 65, 64, 66, 67, 65, 63, 62, 61],
        'High Risk %': [12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trend_data['Month'], y=trend_data['Avg Risk Score'],
                            mode='lines+markers', name='Average Risk Score',
                            line=dict(color='#1f77b4', width=3)))
    fig.add_trace(go.Scatter(x=trend_data['Month'], y=trend_data['High Risk %'],
                            mode='lines+markers', name='High Risk %',
                            line=dict(color='#ff7f0e', width=3)))
    
    fig.update_layout(title="Risk Metrics Over Time", height=400)
    st.plotly_chart(fig, use_container_width=True)
