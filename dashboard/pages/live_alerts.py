import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import sqlite3
import pandas as pd
import streamlit as st

from dashboard.components.tables import show_alerts_table

DB_PATH = ROOT_DIR / "cyber_monitor.db"


def load_alerts():
    conn = sqlite3.connect(DB_PATH)
    alerts_df = pd.read_sql_query("SELECT * FROM alerts ORDER BY id DESC", conn)
    conn.close()
    return alerts_df


st.title("🚨 Live Alerts")

alerts_df = load_alerts()

severity_filter = st.multiselect(
    "Filter by Severity",
    options=["LOW", "MEDIUM", "HIGH", "CRITICAL"],
    default=["LOW", "MEDIUM", "HIGH", "CRITICAL"]
)

if not alerts_df.empty and "severity" in alerts_df.columns:
    alerts_df = alerts_df[alerts_df["severity"].isin(severity_filter)]

show_alerts_table(alerts_df, limit=50)