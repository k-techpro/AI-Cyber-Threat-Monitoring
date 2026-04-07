# 🛡️ AI Cyber Threat Monitoring System

A real-time cyber threat detection and monitoring system that simulates network activity, detects suspicious behavior, and visualizes alerts and incidents through an interactive dashboard.

---

## 🚀 Features

- 🔄 Real-time log simulation
- ⚠️ Threat detection (rule-based)
- 🚨 Alert & Incident generation
- 📊 Interactive Streamlit dashboard
- 🔌 REST API using FastAPI
- 🗄️ SQLite database integration

---

## 🧠 Detection Logic

The system detects threats based on:

- Multiple failed login attempts
- High request frequency (Bot / DDoS)
- Login from new IP/device
- Unusual login time or location

---

## 🖥️ Tech Stack

- Python
- FastAPI
- Streamlit
- SQLite
- SQLAlchemy

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

python -m scripts.init_db

python -m scripts.seed_data

python -m scripts.run_pipeline

uvicorn app.main:app --reload

streamlit run dashboard/streamlit_app.py

📊 API Endpoints
/logs
/alerts
/analytics
/analytics/top-ips

