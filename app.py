import streamlit as st
from log_analyzer import extract_errors, run_local_llm
import os

st.set_page_config(page_title="CI/CD Log AI Helper", layout="wide")
st.title(" CI/CD Log Analyzer with Local LLM (Ollama)")

log = st.text_area("Paste your CI/CD log here:", height=300)

if st.button("Analyze Log"):
    with st.spinner("Analyzing..."):
        errors = extract_errors(log)
        prompt = f"You are a DevOps expert. This CI/CD log failed:\n{errors}\n\nWhat caused the issue and how to fix it?"
        result = run_local_llm(prompt)
        st.subheader(" AI Suggestion:")
        st.code(result, language='text')
