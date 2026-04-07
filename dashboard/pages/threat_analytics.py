import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import sqlite3
import pandas as pd
import streamlit as st

from dashboard.components.charts import (
    threat_type_pie,
    severity_bar,
    top_ips_chart,
    threat_trend_chart
)

DB_PATH = ROOT_DIR / "cyber_monitor.db"


def load_alerts():
    conn = sqlite3.connect(DB_PATH)
    alerts_df = pd.read_sql_query("SELECT * FROM alerts ORDER BY id DESC", conn)
    conn.close()
    return alerts_df


st.title("🧠 Threat Analytics")

alerts_df = load_alerts()

threat_type_pie(alerts_df)
severity_bar(alerts_df)
top_ips_chart(alerts_df)
threat_trend_chart(alerts_df)