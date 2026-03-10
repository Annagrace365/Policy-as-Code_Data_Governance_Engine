import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipeline.run_pipeline import run_governance_pipeline

st.set_page_config(page_title="Content Governance Engine")

st.title("Content Governance Engine")
st.write("Detect and sanitize sensitive data based on governance policies.")

# User input
user_input = st.text_area("Enter text to analyze")

# Process button
if st.button("Run Governance Check"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = run_governance_pipeline(user_input)

        st.subheader("Sanitized Output")
        st.success(result)