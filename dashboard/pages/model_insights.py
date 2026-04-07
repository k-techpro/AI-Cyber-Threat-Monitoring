from pathlib import Path
import streamlit as st
import pandas as pd

try:
    from app.ml.predict import ThreatPredictor
    MODEL_AVAILABLE = True
except Exception:
    MODEL_AVAILABLE = False


st.title("🤖 Model Insights")

st.subheader("Model Status")
if MODEL_AVAILABLE:
    st.success("Threat prediction model is available.")
else:
    st.warning("Model artifacts not found yet. Train the model first.")

st.markdown("---")
st.subheader("Sample Prediction")

sample_event = {
    "failed_attempts": 6,
    "request_count": 120,
    "is_new_ip": 1,
    "is_new_device": 1,
    "location": "Unknown",
    "login_hour": 2
}

st.json(sample_event)

if MODEL_AVAILABLE:
    try:
        predictor = ThreatPredictor()
        result = predictor.predict_event(sample_event)
        st.success(f"Prediction: {result['prediction']}")
        st.info(f"Probability: {result['probability']}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
else:
    st.info("Run model training first to enable predictions.")