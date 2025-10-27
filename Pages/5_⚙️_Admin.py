import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Admin - KCB SmartCredit",
    page_icon="⚙️",
    layout="wide"
)

# Custom CSS for admin panel
st.markdown("""
<style>
    .admin-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #6c757d;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .system-health-good { border-left: 5px solid #28a745; }
    .system-health-warning { border-left: 5px solid #ffc107; }
    .system-health-critical { border-left: 5px solid #dc3545; }
    .log-info { color: #17a2b8; }
    .log-warning { color: #ffc107; font-weight: bold; }
    .log-error { color: #dc3545; font-weight: bold; }
    .user-active { color: #28a745; font-weight: bold; }
    .user-inactive { color: #6c757d; }
</style>
""", unsafe_allow_html=True)

st.title("⚙️ Admin Panel")
st.markdown("System configuration and management")

tab1, tab2, tab3, tab4 = st.tabs(["🧠 Model Management", "📊 System Monitoring", "👥 User Management", "⚡ Configuration"])

with tab1:
    st.subheader("🧠 ML Model Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**Model Version Control**")
        st.selectbox("Active Risk Model Version", ["v2.1.0 (Production)", "v2.0.0", "v1.5.0"], key="risk_model")
        st.selectbox("NPL Forecast Model", ["v1.2.0 (Production)", "v1.1.0"], key="npl_model")
        st.selectbox("Restructuring Optimizer", ["v1.0.0 (Production)"], key="restructure_model")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**Training Configuration**")
        st.number_input("Retraining Frequency (Days)", value=30, min_value=1, max_value=90, key="retrain_freq")
        st.number_input("Data Lookback Period (Months)", value=24, min_value=6, max_value=60, key="lookback")
        st.slider("Model Confidence Threshold", 0.5, 0.95, 0.75, 0.05, key="confidence_threshold")
        
        train_col1, train_col2 = st.columns(2)
        with train_col1:
            if st.button("🔄 Schedule Retraining", use_container_width=True):
                st.success("Model retraining scheduled for tonight!")
        with train_col2:
            if st.button("🚀 Deploy to Production", use_container_width=True):
                st.info("Model deployment initiated...")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.subheader("📈 Model Performance")
        
        performance_data = pd.DataFrame({
            'Model': ['Risk Assessment', 'NPL Forecast', 'Restructuring', 'Credit Scoring'],
            'Accuracy': [87.3, 92.1, 78.5, 85.2],
            'Precision': [85.6, 89.7, 82.3, 83.8],
            'Recall': [88.9, 93.4, 76.8, 86.5],
            'F1-Score': [87.2, 91.5, 79.4, 85.1],
            'Last Updated': ['2 hours ago', '1 day ago', '3 days ago', '6 hours ago'],
            'Status': ['✅ Stable', '✅ Stable', '⚠️ Monitoring', '✅ Stable']
        })
        
        # Style the performance data
        def style_performance(val):
            if isinstance(val, (int, float)):
                if val > 90:
                    return 'color: #28a745; font-weight: bold;'
                elif val > 80:
                    return 'color: #20c997; font-weight: bold;'
                elif val > 70:
                    return 'color: #ffc107; font-weight: bold;'
                else:
                    return 'color: #dc3545; font-weight: bold;'
            return ''
        
        st.dataframe(
            performance_data.style.applymap(style_performance, subset=['Accuracy', 'Precision', 'Recall', 'F1-Score']),
            use_container_width=True,
            hide_index=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Model drift monitoring
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.subheader("📊 Data Drift Monitoring")
        
        drift_col1, drift_col2, drift_col3 = st.columns(3)
        with drift_col1:
            st.metric("Feature Drift Score", "0.8%", "-0.2%")
        with drift_col2:
            st.metric("Concept Drift Score", "1.2%", "+0.3%")
        with drift_col3:
            st.metric("Data Quality Score", "98.5%", "+0.5%")
        
        # Drift history
        st.write("**Drift History (Last 7 Days)**")
        drift_history = pd.DataFrame({
            'Date': ['01-15', '01-14', '01-13', '01-12', '01-11', '01-10', '01-09'],
            'Feature Drift': [0.8, 1.0, 0.9, 1.1, 1.3, 1.2, 1.4],
            'Concept Drift': [1.2, 1.0, 1.1, 0.9, 1.2, 1.3, 1.1]
        })
        st.line_chart(drift_history.set_index('Date'))
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("📊 System Health Monitoring")
    
    # System metrics with health indicators
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="admin-card system-health-good">', unsafe_allow_html=True)
        st.metric("API Response Time", "142ms", "-8ms")
        st.progress(85, text="Performance: 85%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="admin-card system-health-good">', unsafe_allow_html=True)
        st.metric("Database Connections", "24/50", "+2")
        st.progress(48, text="Capacity: 48%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="admin-card system-health-good">', unsafe_allow_html=True)
        st.metric("Active Users", "17", "+3")
        st.progress(34, text="Utilization: 34%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="admin-card system-health-good">', unsafe_allow_html=True)
        st.metric("Error Rate", "0.2%", "-0.1%")
        st.progress(98, text="Reliability: 98%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional system metrics
    st.subheader("🖥️ Resource Utilization")
    
    res_col1, res_col2, res_col3, res_col4 = st.columns(4)
    
    with res_col1:
        st.metric("CPU Usage", "45%", "+5%")
    
    with res_col2:
        st.metric("Memory Usage", "68%", "+3%")
    
    with res_col3:
        st.metric("Disk I/O", "23%", "-2%")
    
    with res_col4:
        st.metric("Network Latency", "28ms", "+2ms")
    
    # System logs with enhanced styling
    st.subheader("📋 Recent System Logs")
    
    logs_data = pd.DataFrame({
        'Timestamp': [
            '2024-01-15 14:23:45',
            '2024-01-15 14:20:12', 
            '2024-01-15 14:15:33',
            '2024-01-15 14:10:21',
            '2024-01-15 14:05:47',
            '2024-01-15 13:58:32',
            '2024-01-15 13:45:18'
        ],
        'Level': ['INFO', 'WARNING', 'INFO', 'ERROR', 'INFO', 'INFO', 'WARNING'],
        'Message': [
            'Risk assessment completed for BORR001',
            'High memory usage detected in ML module',
            'Daily backup completed successfully',
            'Database connection timeout - retrying',
            'User login: admin@kcb.com',
            'Scheduled model validation completed',
            'API response time above threshold'
        ],
        'Component': ['ML Engine', 'System', 'Backup', 'Database', 'Auth', 'ML Engine', 'API Gateway']
    })
    
    # Style logs based on level
    def style_logs(row):
        if row['Level'] == 'ERROR':
            return ['background-color: #f8d7da'] * len(row)
        elif row['Level'] == 'WARNING':
            return ['background-color: #fff3cd'] * len(row)
        else:
            return [''] * len(row)
    
    st.dataframe(
        logs_data.style.apply(style_logs, axis=1),
        use_container_width=True,
        hide_index=True
    )
    
    # Log actions
    log_col1, log_col2, log_col3 = st.columns(3)
    with log_col1:
        if st.button("🔄 Refresh Logs", use_container_width=True):
            st.rerun()
    with log_col2:
        if st.button("📥 Export Logs", use_container_width=True):
            st.success("Logs exported successfully!")
    with log_col3:
        if st.button("🧹 Clear Old Logs", use_container_width=True):
            st.info("Logs older than 30 days cleared")

with tab3:
    st.subheader("👥 User Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**Add New User**")
        new_email = st.text_input("Email Address", placeholder="user@kcb.com")
        new_role = st.selectbox("Role", ["Risk Analyst", "Credit Officer", "Admin", "View Only", "Auditor"])
        new_name = st.text_input("Full Name", placeholder="John Doe")
        new_department = st.selectbox("Department", ["Risk Management", "Credit", "IT", "Operations", "Compliance"])
        
        user_col1, user_col2 = st.columns(2)
        with user_col1:
            if st.button("➕ Create User", use_container_width=True, type="primary"):
                if new_email and new_name:
                    st.success(f"User {new_name} created successfully!")
                else:
                    st.error("Please fill in all required fields")
        with user_col2:
            if st.button("📧 Send Invite", use_container_width=True):
                st.info("Invitation email sent to user")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**User Accounts**")
        users_data = pd.DataFrame({
            'User': ['admin@kcb.com', 'risk.analyst@kcb.com', 'credit.officer@kcb.com', 'auditor@kcb.com', 'view.only@kcb.com'],
            'Name': ['System Admin', 'Jane Smith', 'Mike Johnson', 'Sarah Wilson', 'David Brown'],
            'Role': ['Admin', 'Risk Analyst', 'Credit Officer', 'Auditor', 'View Only'],
            'Department': ['IT', 'Risk Management', 'Credit', 'Compliance', 'Operations'],
            'Last Login': ['2 hours ago', '1 day ago', '3 days ago', '1 week ago', '2 weeks ago'],
            'Status': ['Active', 'Active', 'Active', 'Inactive', 'Active']
        })
        
        # Style user status
        def style_user_status(val):
            if val == 'Active':
                return 'user-active'
            else:
                return 'user-inactive'
        
        styled_users = users_data.copy()
        styled_users['Status'] = styled_users['Status'].apply(style_user_status)
        
        st.dataframe(styled_users, use_container_width=True, hide_index=True)
        
        # User management actions
        action_col1, action_col2 = st.columns(2)
        with action_col1:
            st.selectbox("Select User", users_data['User'].tolist(), key="user_select")
        with action_col2:
            if st.button("👤 Manage User", use_container_width=True):
                st.info("User management panel opened")
        st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.subheader("⚡ System Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**Risk Thresholds**")
        st.number_input("Risk Score Threshold - Critical", value=80, min_value=70, max_value=95, key="critical_thresh")
        st.number_input("Risk Score Threshold - High", value=60, min_value=50, max_value=80, key="high_thresh")
        st.number_input("Risk Score Threshold - Medium", value=40, min_value=30, max_value=60, key="medium_thresh")
        st.number_input("NPL Alert Threshold (%)", value=10.0, min_value=5.0, max_value=20.0, step=0.5, key="npl_thresh")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**System Settings**")
        st.number_input("Session Timeout (Minutes)", value=30, min_value=5, max_value=120, key="session_timeout")
        st.number_input("Max Login Attempts", value=5, min_value=3, max_value=10, key="max_logins")
        st.selectbox("Default Language", ["English", "Swahili", "French"], key="language")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**Restructuring Rules**")
        st.number_input("Max Restructuring Term (Months)", value=60, min_value=12, max_value=84, key="max_term")
        st.number_input("Min Payment Reduction (%)", value=10.0, min_value=5.0, max_value=50.0, step=1.0, key="min_reduction")
        st.number_input("Max Interest Rate Reduction (%)", value=5.0, min_value=1.0, max_value=10.0, step=0.5, key="max_interest_red")
        st.number_input("Auto-approval Limit (KES)", value=50000, min_value=10000, max_value=200000, step=10000, key="auto_approval")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="admin-card">', unsafe_allow_html=True)
        st.write("**Notification Settings**")
        st.checkbox("Email Alerts", value=True, key="email_alerts")
        st.checkbox("SMS Notifications", value=True, key="sms_alerts")
        st.checkbox("Push Notifications", value=False, key="push_alerts")
        st.number_input("Alert Frequency (Hours)", value=4, min_value=1, max_value=24, key="alert_freq")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Configuration actions
    config_col1, config_col2, config_col3 = st.columns(3)
    with config_col1:
        if st.button("💾 Save Configuration", type="primary", use_container_width=True):
            st.success("Configuration saved successfully!")
    with config_col2:
        if st.button("🔄 Reset to Defaults", use_container_width=True):
            st.warning("Configuration reset to default values")
    with config_col3:
        if st.button("📤 Export Config", use_container_width=True):
            st.info("Configuration exported to file")

# Footer with system info
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.caption(f"🕒 Last System Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
with footer_col2:
    st.caption("🔐 System Version: KCB SmartCredit v2.1.0")
with footer_col3:
    st.caption("🏢 Environment: Production")
