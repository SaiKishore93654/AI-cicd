import subprocess
import socket
import time
import webbrowser

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if not is_port_open(8501):
    print("🚀 Starting Streamlit dashboard...")
    subprocess.Popen(["streamlit", "run", "app.py"], shell=True)
    time.sleep(5)  # Give Streamlit time to start

# Open browser tab
webbrowser.open("http://localhost:8501", new=2)
