import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import sqlite3
import pandas as pd
import streamlit as st

from dashboard.components.tables import show_incidents_table

DB_PATH = ROOT_DIR / "cyber_monitor.db"


def load_incidents():
    conn = sqlite3.connect(DB_PATH)
    try:
        incidents_df = pd.read_sql_query("SELECT * FROM incidents ORDER BY id DESC", conn)
    except Exception:
        incidents_df = pd.DataFrame()
    conn.close()
    return incidents_df


st.title("📁 Incident History")

incidents_df = load_incidents()
show_incidents_table(incidents_df, limit=50)