import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="Banking Integration - KCB SmartCredit",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS for integration page
st.markdown("""
<style>
    .integration-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .system-status {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 5px solid;
    }
    .status-connected { border-left-color: #28a745; background-color: #d4edda; }
    .status-pending { border-left-color: #ffc107; background-color: #fff3cd; }
    .status-disconnected { border-left-color: #dc3545; background-color: #f8d7da; }
    .data-flow {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 2px dashed #dee2e6;
        margin: 0.5rem 0;
    }
    .api-metric {
        text-align: center;
        padding: 1rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🌐 Real-Time Banking Integration")
    st.markdown("Live connections to KCB core banking systems and external data sources")
    
    # System Status Overview
    st.subheader("🖥️ System Integration Status")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="system-status status-connected">', unsafe_allow_html=True)
        st.metric("Core Banking (T24)", "Connected", "Live")
        st.caption("Last sync: 2 min ago")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="system-status status-connected">', unsafe_allow_html=True)
        st.metric("M-Pesa Gateway", "Connected", "2,347 txns")
        st.caption("Real-time monitoring")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="system-status status-pending">', unsafe_allow_html=True)
        st.metric("Credit Bureau", "Syncing", "85%")
        st.caption("Refresh in progress")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="system-status status-connected">', unsafe_allow_html=True)
        st.metric("Transaction API", "Connected", "Active")
        st.caption("All channels live")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Real-time Data Flow
    st.subheader("📊 Live Data Integration Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Core Banking Integration
        st.markdown('<div class="integration-card">', unsafe_allow_html=True)
        st.write("**🏦 Core Banking System (T24)**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Real-time data metrics
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.markdown('<div class="api-metric">', unsafe_allow_html=True)
            st.metric("Active Loans", "1,247", "+18")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with metric_col2:
            st.markdown('<div class="api-metric">', unsafe_allow_html=True)
            st.metric("Portfolio Value", "KES 245.7M", "+2.1%")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with metric_col3:
            st.markdown('<div class="api-metric">', unsafe_allow_html=True)
            st.metric("Sync Latency", "142ms", "-8ms")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Recent core banking updates
        st.write("**🔄 Recent Core Banking Updates**")
        core_updates = [
            {"time": "2 min ago", "action": "Loan disbursement", "amount": "KES 500,000", "customer": "John Mwangi"},
            {"time": "5 min ago", "payment": "M-Pesa repayment", "amount": "KES 15,000", "loan": "LN04521"},
            {"time": "8 min ago", "action": "Account update", "details": "Contact information", "customer": "Sarah K."},
            {"time": "12 min ago", "payment": "Bank transfer", "amount": "KES 45,000", "loan": "LN07893"}
        ]
        
        for update in core_updates:
            with st.container():
                cols = st.columns([1, 2, 1])
                cols[0].write(f"`{update['time']}`")
                cols[1].write(f"**{update.get('action', update.get('payment', 'Update'))}**")
                cols[2].write(update['amount'] if 'amount' in update else "Updated")
                st.divider()
    
    with col2:
        # Payment Channel Integration
        st.markdown('<div class="integration-card">', unsafe_allow_html=True)
        st.write("**📱 Payment Channel Monitoring**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Payment channels metrics
        pay_col1, pay_col2, pay_col3 = st.columns(3)
        
        with pay_col1:
            st.markdown('<div class="api-metric">', unsafe_allow_html=True)
            st.metric("M-Pesa Today", "2,347", "+124")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with pay_col2:
            st.markdown('<div class="api-metric">', unsafe_allow_html=True)
            st.metric("Bank Transfers", "856", "+32")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with pay_col3:
            st.markdown('<div class="api-metric">', unsafe_allow_html=True)
            st.metric("Card Payments", "423", "+18")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Real-time transaction feed
        st.write("**💳 Live Transaction Stream**")
        
        # Simulate live transactions
        if 'transactions' not in st.session_state:
            st.session_state.transactions = []
        
        if st.button("🔄 Refresh Transactions"):
            # Generate sample transactions
            channels = ["M-Pesa", "Bank Transfer", "Visa Card", "MasterCard"]
            customers = ["John Doe", "Jane Smith", "Mike Johnson", "Sarah Wilson", "David Brown"]
            
            new_transaction = {
                "time": datetime.now().strftime("%H:%M:%S"),
                "channel": random.choice(channels),
                "amount": f"KES {random.randint(1000, 50000):,}",
                "customer": random.choice(customers),
                "type": random.choice(["Repayment", "Loan Disbursement", "Fee Payment"])
            }
            st.session_state.transactions.insert(0, new_transaction)
            
            # Keep only last 10 transactions
            st.session_state.transactions = st.session_state.transactions[:10]
        
        # Display transactions
        for txn in st.session_state.transactions:
            with st.container():
                col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
                col1.write(f"`{txn['time']}`")
                col2.write(f"**{txn['channel']}**")
                col3.write(txn['amount'])
                col4.write(txn['type'])
    
    # Credit Bureau Integration
    st.subheader("📋 Credit Bureau Data Integration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🏛️ Credit Reference Bureau (CRB)**")
        
        # Bureau metrics
        bureau_col1, bureau_col2 = st.columns(2)
        
        with bureau_col1:
            st.metric("Records Synced", "45,782", "92%")
            st.metric("Average Score", "642", "+8")
        
        with bureau_col2:
            st.metric("Update Frequency", "Hourly", "Live")
            st.metric("Data Quality", "98.5%", "+1.2%")
        
        # Bureau status
        st.write("**Sync Status**")
        progress = st.progress(85, text="Credit data synchronization: 85%")
        
        if st.button("🔄 Force Refresh Bureau Data"):
            with st.spinner("Refreshing credit bureau data..."):
                time.sleep(2)
                st.success("Credit bureau data refreshed successfully!")
    
    with col2:
        st.write("**📊 Credit Score Distribution**")
        
        # Generate sample credit score distribution
        score_ranges = ['300-500', '501-600', '601-700', '701-850']
        counts = [1250, 2340, 1560, 890]
        
        score_data = pd.DataFrame({
            'Score Range': score_ranges,
            'Borrowers': counts
        })
        
        st.bar_chart(score_data.set_index('Score Range')['Borrowers'])
    
    # API Configuration & Monitoring
    st.subheader("⚙️ Integration Configuration")
    
    tab1, tab2, tab3 = st.tabs(["API Settings", "Data Mapping", "Monitoring"])
    
    with tab1:
        st.write("**API Connection Settings**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.text_input("Core Banking API URL", 
                         value="https://api.kcb.co.ke/t24/v1/", 
                         type="password")
            st.text_input("API Key", value="••••••••••••••••", type="password")
            st.number_input("Sync Interval (minutes)", value=5, min_value=1, max_value=60)
        
        with col2:
            st.text_input("M-Pesa Gateway URL",
                         value="https://api.safaricom.co.ke/mpesa/",
                         type="password")
            st.text_input("Credit Bureau API",
                         value="https://crb.creditinfo.co.ke/api/v2/",
                         type="password")
            st.selectbox("Data Encryption", ["AES-256", "RSA-2048", "TLS 1.3"])
        
        if st.button("💾 Save API Configuration", type="primary"):
            st.success("API configuration saved successfully!")
    
    with tab2:
        st.write("**Data Field Mapping**")
        
        mapping_data = pd.DataFrame({
            'KCB Field': ['CustomerID', 'LoanAmount', 'OutstandingBalance', 'LastPaymentDate', 'ProductType'],
            'External System': ['ClientID', 'Principal', 'CurrentBalance', 'PaymentDate', 'LoanProduct'],
            'Status': ['✅ Mapped', '✅ Mapped', '🔄 Syncing', '✅ Mapped', '⚠️ Review'],
            'Last Sync': ['2 min ago', '2 min ago', 'Updating...', '5 min ago', '1 hour ago']
        })
        
        st.dataframe(mapping_data, use_container_width=True, hide_index=True)
        
        if st.button("🔄 Validate Data Mapping"):
            st.info("Data mapping validation in progress...")
            time.sleep(2)
            st.success("All data mappings validated successfully!")
    
    with tab3:
        st.write("**System Performance Monitoring**")
        
        # API performance metrics
        perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4)
        
        with perf_col1:
            st.metric("API Uptime", "99.98%", "+0.02%")
        
        with perf_col2:
            st.metric("Avg Response Time", "156ms", "-12ms")
        
        with perf_col3:
            st.metric("Error Rate", "0.12%", "-0.03%")
        
        with perf_col4:
            st.metric("Data Throughput", "2.4 GB/hr", "+0.3 GB")
        
        # Performance chart
        st.write("**API Response Time Trend**")
        time_data = pd.DataFrame({
            'Hour': [f"{i}:00" for i in range(24)],
            'Response Time (ms)': [180 + random.randint(-20, 20) for _ in range(24)]
        })
        st.line_chart(time_data, x='Hour', y='Response Time (ms)')
    
    # Data Quality & Validation
    st.subheader("🔍 Data Quality Assessment")
    
    quality_col1, quality_col2, quality_col3 = st.columns(3)
    
    with quality_col1:
        st.metric("Data Completeness", "98.7%", "+1.2%")
        st.metric("Record Accuracy", "99.2%", "+0.8%")
    
    with quality_col2:
        st.metric("Timeliness", "99.5%", "+0.5%")
        st.metric("Consistency", "97.8%", "+1.5%")
    
    with quality_col3:
        st.metric("Validation Score", "98.4%", "+2.1%")
        st.metric("Duplicate Rate", "0.3%", "-0.2%")
    
    # Integration Actions
    st.markdown("---")
    st.subheader("🚀 Integration Actions")
    
    action_col1, action_col2, action_col3, action_col4 = st.columns(4)
    
    with action_col1:
        if st.button("🔄 Full Data Sync", use_container_width=True):
            with st.spinner("Initiating full data synchronization..."):
                time.sleep(3)
                st.success("Full data sync completed successfully!")
    
    with action_col2:
        if st.button("📊 Generate API Report", use_container_width=True):
            st.info("API performance report generated!")
    
    with action_col3:
        if st.button("🔍 Run Data Audit", use_container_width=True):
            st.info("Data quality audit initiated...")
    
    with action_col4:
        if st.button("📧 Support Ticket", use_container_width=True):
            st.info("Integration support ticket created!")
    
    # Footer with last update
    st.markdown("---")
    st.caption(f"🌐 Last system check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Integration Dashboard v2.1")

if __name__ == "__main__":
    main()