import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import sqlite3
import pandas as pd
import streamlit as st

from dashboard.components.metric_cards import show_metric_cards
from dashboard.components.charts import (
    threat_type_pie,
    severity_bar,
    top_ips_chart,
    threat_trend_chart
)

DB_PATH = ROOT_DIR / "cyber_monitor.db"


def load_data():
    conn = sqlite3.connect(DB_PATH)
    logs_df = pd.read_sql_query("SELECT * FROM logs ORDER BY id DESC", conn)
    alerts_df = pd.read_sql_query("SELECT * FROM alerts ORDER BY id DESC", conn)
    conn.close()
    return logs_df, alerts_df


st.title("📊 Overview")

logs_df, alerts_df = load_data()

total_logs = len(logs_df)
total_alerts = len(alerts_df)
critical_alerts = len(alerts_df[alerts_df["severity"] == "CRITICAL"]) if not alerts_df.empty else 0
high_alerts = len(alerts_df[alerts_df["severity"] == "HIGH"]) if not alerts_df.empty else 0

show_metric_cards(total_logs, total_alerts, critical_alerts, high_alerts)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    threat_type_pie(alerts_df)
with col2:
    severity_bar(alerts_df)

st.markdown("---")

col3, col4 = st.columns(2)
with col3:
    top_ips_chart(alerts_df)
with col4:
    threat_trend_chart(alerts_df)