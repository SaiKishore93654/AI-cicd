import socket
import subprocess
import time
import os

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if is_port_in_use(8501):
    print("Streamlit already running.")
else:
    print("Starting Streamlit dashboard...")
    # Launch in a visible terminal using cmd
    subprocess.Popen(
        'start cmd /k streamlit run app.py',
        shell=True
    )
    time.sleep(5)
