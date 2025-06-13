import subprocess
import time
import requests
import webbrowser
import os

def is_streamlit_running():
    try:
        r = requests.get("http://localhost:8501", timeout=2)
        return r.status_code == 200
    except:
        return False

if not is_streamlit_running():
    print("Starting Streamlit dashboard...")
    subprocess.Popen("start cmd /k streamlit run app.py", shell=True)
    time.sleep(5)
    webbrowser.open("http://localhost:8501")
else:
    print("Streamlit is already running.")
