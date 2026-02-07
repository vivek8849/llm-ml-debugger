import streamlit as st
import requests

API_URL = "http://api:8000/debug-report"

st.set_page_config(page_title="ML Debug Dashboard", layout="centered")

st.title("🧠 ML Debug & Evaluation Dashboard")
st.markdown(
    """
This dashboard demonstrates **ML model evaluation and debugging**
using **cost-aware metrics** and **LLM-based reasoning**.

The LLM acts as a *reasoning assistant*, not a decision-maker.
"""
)

st.subheader("📊 Enter ML Evaluation Summary")

summary = st.text_area(
    "Paste evaluation summary here:",
    height=200,
    placeholder="Example:\nBaseline model shows high false negatives due to class imbalance..."
)

if st.button("Generate ML Debug Report"):
    if not summary.strip():
        st.warning("Please enter an evaluation summary.")
    else:
        with st.spinner("Analyzing model behavior..."):
            response = requests.post(API_URL, json={"summary": summary})

            if response.status_code == 200:
                report = response.json()["debug_report"]
                st.subheader("📝 LLM-Based ML Debug Report")
                st.write(report)
            else:
                st.error("Failed to generate debug report.")