import streamlit as st
import plotly.express as px
import pandas as pd


def threat_type_pie(alerts_df: pd.DataFrame):
    if alerts_df.empty:
        st.info("No alerts available.")
        return

    fig = px.pie(
        alerts_df,
        names="threat_type",
        title="Threat Type Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)


def severity_bar(alerts_df: pd.DataFrame):
    if alerts_df.empty:
        st.info("No severity data available.")
        return

    severity_counts = alerts_df["severity"].value_counts().reset_index()
    severity_counts.columns = ["severity", "count"]

    fig = px.bar(
        severity_counts,
        x="severity",
        y="count",
        title="Severity Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)


def top_ips_chart(alerts_df: pd.DataFrame):
    if alerts_df.empty:
        st.info("No suspicious IP data available.")
        return

    top_ips = alerts_df["ip_address"].value_counts().reset_index()
    top_ips.columns = ["ip_address", "count"]

    fig = px.bar(
        top_ips.head(10),
        x="ip_address",
        y="count",
        title="Top Suspicious IPs"
    )
    st.plotly_chart(fig, use_container_width=True)


def threat_trend_chart(alerts_df: pd.DataFrame):
    if alerts_df.empty:
        st.info("No alert trend data available.")
        return

    df = alerts_df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["minute"] = df["timestamp"].dt.strftime("%H:%M")

    trend = df.groupby("minute").size().reset_index(name="count")

    fig = px.line(
        trend,
        x="minute",
        y="count",
        markers=True,
        title="Threat Trend Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)