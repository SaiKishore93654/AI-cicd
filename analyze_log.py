import subprocess
import sys

def analyze_log(log_text):
    ollama_cmd = [
        r"C:\Users\saiki\AppData\Local\Programs\Ollama\ollama.exe",
        "run", "llama3"
    ]
    prompt = f"Analyze the following Jenkins log and identify errors or issues:\n\n{log_text}"
    
    process = subprocess.Popen(
        ollama_cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(prompt)
    if stderr:
        print("Error:", stderr)
    print("AI Analysis:\n", stdout)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_logs.py <log_file>")
        sys.exit(1)

    log_path = sys.argv[1]
    with open(log_path, "r") as file:
        logs = file.read()

    analyze_log(logs)
