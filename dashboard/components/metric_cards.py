import streamlit as st


def show_metric_cards(total_logs, total_alerts, critical_alerts, high_alerts):
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Logs", total_logs)
    c2.metric("Total Alerts", total_alerts)
    c3.metric("Critical Alerts", critical_alerts)
    c4.metric("High Alerts", high_alerts)