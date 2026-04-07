# Module Flow

## Step 1: Simulator
attack_simulator.py generates fake logs

## Step 2: Ingestor
log_ingestor.py saves logs to DB

## Step 3: Rule Engine
rule_detector.py detects threats

## Step 4: Alert Service
alert_service.py creates alerts

## Step 5: Incident Service
incident_service.py creates incidents

## Step 6: Scheduler
scheduler.py runs everything continuously

## Step 7: Dashboard
Streamlit displays live data