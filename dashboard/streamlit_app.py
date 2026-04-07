import streamlit as st

st.set_page_config(
    page_title="AI Cyber Threat Monitoring Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🛡️ AI Cyber Threat Monitoring Dashboard")
st.markdown(
    """
    Welcome to the real-time cyber threat monitoring system.

    Use the sidebar to navigate through:
    - Overview
    - Live Alerts
    - Threat Analytics
    - Incident History
    - Model Insights
    """
)