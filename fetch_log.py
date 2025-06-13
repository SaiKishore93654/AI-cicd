import requests
from requests.auth import HTTPBasicAuth
import subprocess
import sys
import webbrowser
import time

# Jenkins config
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "AI-CICD"
USERNAME = "helloworld"
API_TOKEN = "11cb8b0241218b62985fdf4022eff0852a"

# Ollama & dashboard settings
DASHBOARD_URL = "http://localhost:8501"
DASHBOARD_SCRIPT = "app.py"  # your Streamlit file

def fetch_last_build_log():
    crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    auth = HTTPBasicAuth(USERNAME, API_TOKEN)

    crumb_resp = requests.get(crumb_url, auth=auth)
    if crumb_resp.status_code != 200:
        print(f" Failed to get crumb: {crumb_resp.status_code} {crumb_resp.text}")
        sys.exit(1)

    crumb_data = crumb_resp.json()
    headers = {crumb_data['crumbRequestField']: crumb_data['crumb']}

    log_url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    log_resp = requests.get(log_url, auth=auth, headers=headers)

    if log_resp.status_code == 200:
        return log_resp.text
    else:
        print(f" Failed to fetch logs: {log_resp.status_code} {log_resp.text}")
        sys.exit(1)

def save_log_to_file(log_data, filename="jenkins_log.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(log_data)
    print(f" Log saved to {filename}")
    return filename

def analyze_log_with_ollama(filename):
    print(" Analyzing with Ollama...")
    result = subprocess.run(["python", "analyze_logs.py", filename])
    if result.returncode != 0:
        print(" Analysis failed.")
    else:
        print(" Analysis completed.")

def start_streamlit_if_needed():
    print(" Starting Streamlit dashboard...")
    subprocess.Popen(["streamlit", "run", DASHBOARD_SCRIPT])
    time.sleep(5)
    print(" Opening dashboard...")
    webbrowser.open(DASHBOARD_URL)

if __name__ == "__main__":
    log_data = fetch_last_build_log()
    log_file = save_log_to_file(log_data)
    analyze_log_with_ollama(log_file)
    start_streamlit_if_needed()
