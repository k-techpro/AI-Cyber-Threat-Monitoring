import streamlit as st
import pandas as pd


def show_alerts_table(alerts_df: pd.DataFrame, limit: int = 20):
    if alerts_df.empty:
        st.info("No alerts available.")
        return

    cols = [
        "timestamp", "username", "ip_address",
        "threat_type", "severity", "risk_score", "reason"
    ]
    available_cols = [c for c in cols if c in alerts_df.columns]

    st.dataframe(
        alerts_df[available_cols].head(limit),
        use_container_width=True
    )


def show_logs_table(logs_df: pd.DataFrame, limit: int = 20):
    if logs_df.empty:
        st.info("No logs available.")
        return

    cols = [
        "timestamp", "username", "ip_address",
        "status", "failed_attempts", "request_count", "event_type"
    ]
    available_cols = [c for c in cols if c in logs_df.columns]

    st.dataframe(
        logs_df[available_cols].head(limit),
        use_container_width=True
    )


def show_incidents_table(incidents_df: pd.DataFrame, limit: int = 20):
    if incidents_df.empty:
        st.info("No incidents available.")
        return

    st.dataframe(
        incidents_df.head(limit),
        use_container_width=True
    )