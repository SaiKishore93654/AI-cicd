import socket
import subprocess
import time
import os

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if is_port_in_use(8501):
    print("✅ Streamlit already running on port 8501.")
else:
    print("🚀 Starting Streamlit dashboard...")
    subprocess.Popen(
        ["streamlit", "run", "app.py"],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=os.getcwd()
    )
    time.sleep(3)  # wait for server to boot
