import streamlit as st
from pipeline.runner import run_pipeline

st.set_page_config(
    page_title="Data Quality Pipeline",
    layout="wide"
)

st.title("📊 Data Quality Pipeline Dashboard")

result = run_pipeline()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows Processed", result["rows"])

with col2:
    st.metric(
        "Execution Time (sec)",
        result["metrics"]["execution_time_sec"]
    )

with col3:
    st.metric(
        "Estimated Cost ($)",
        result["metrics"]["estimated_cost"]
    )

st.subheader("Cost Breakdown")
st.json(result["metrics"]["cost_breakdown"])

st.subheader("Data Quality Checks")
st.json(result["quality"])
