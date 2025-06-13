# analyze_logs.py
import subprocess

def analyze_log(text):
    process = subprocess.Popen(
        [r"C:\Users\saiki\AppData\Local\Programs\Ollama\ollama.exe", "run", "llama3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(f"Analyze this Jenkins log:\n{text}")
    if stderr:
        print("Error:", stderr)
    print("\n🔍 AI Analysis:\n", stdout)

if __name__ == "__main__":
    with open("jenkins_log.txt", "r") as f:
        logs = f.read()
    analyze_log(logs)
