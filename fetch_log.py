import requests
from requests.auth import HTTPBasicAuth
import sys
import os

# Configuration
JENKINS_URL = "http://localhost:8080"  # Your Jenkins URL
JOB_NAME = "AI-CICD"                   # Your Jenkins job name
USERNAME = "helloworld"                # Jenkins user with API token access
API_TOKEN = "11cb8b0241218b62985fdf4022eff0852a"  # Jenkins API token for USERNAME

def fetch_last_build_log():
    crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    auth = HTTPBasicAuth(USERNAME, API_TOKEN)

    # Get Jenkins CSRF crumb for POST requests
    crumb_resp = requests.get(crumb_url, auth=auth)
    if crumb_resp.status_code != 200:
        print(f"Failed to get crumb: {crumb_resp.status_code} {crumb_resp.text}", file=sys.stderr)
        sys.exit(1)

    crumb_data = crumb_resp.json()
    headers = {crumb_data['crumbRequestField']: crumb_data['crumb']}

    # Fetch last build console text
    log_url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    log_resp = requests.get(log_url, auth=auth, headers=headers)

    if log_resp.status_code == 200:
        return log_resp.text
    else:
        print(f"Failed to fetch logs: {log_resp.status_code} {log_resp.text}", file=sys.stderr)
        sys.exit(1)

def save_log_to_file(log_data, filename="jenkins_log.txt"):
    workspace = os.getcwd()
    safe_path = os.path.join(workspace, "tmp_logs")
    os.makedirs(safe_path, exist_ok=True)
    full_path = os.path.join(safe_path, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(log_data)
    print(f" Log saved to {full_path}")
    return full_path

def open_streamlit_tab():
    import webbrowser
    webbrowser.open("http://localhost:8501", new=2)  # Open in new browser tab

if __name__ == "__main__":
    log_data = fetch_last_build_log()
    log_file = save_log_to_file(log_data)
    open_streamlit_tab()
