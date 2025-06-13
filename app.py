import streamlit as st
from log_analyzer import extract_errors, run_local_llm

st.set_page_config(page_title="CI/CD AI Analyzer", layout="wide")
st.title(" Ollama-Powered CI/CD Log Dashboard")

# Load log file
try:
    with open("jenkins_log.txt", "r", encoding="utf-8") as f:
        log = f.read()
except FileNotFoundError:
    log = ""

st.text_area("CI/CD Log", value=log, height=300, key="log")

if st.button("Analyze Log"):
    errors = extract_errors(log)
    if not errors.strip():
        st.success(" Build successful. No errors.")
    else:
        prompt = f"Analyze the following CI/CD error log and suggest fixes:\n\n{errors}"
        result = run_local_llm(prompt)
        st.error(" Errors found in the build log.")
        st.subheader(" Ollama Suggestion:")
        st.code(result, language="text")
