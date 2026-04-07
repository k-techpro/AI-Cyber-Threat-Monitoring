# AI Cyber Threat Monitoring Dashboard - Architecture

## Overview
This system simulates real-time cybersecurity monitoring using logs, rule-based detection, and ML-based threat analysis.

## Components

### 1. Data Ingestion
- Logs generated from simulator
- Stored in SQLite database

### 2. Detection Layer
- Rule-based detection (brute force, anomalies)
- ML-based detection (future extension)

### 3. Alert System
- Alerts generated based on severity
- Stored and visualized

### 4. Incident Management
- Critical alerts create incidents
- Tracks attack patterns

### 5. Dashboard (Streamlit)
- Live monitoring
- Visual analytics

## Flow
Log → Detection → Alert → Incident → Dashboard