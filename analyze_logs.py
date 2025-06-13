import sys
import requests

log_file = sys.argv[1] if len(sys.argv) > 1 else "jenkins_log.txt"

with open(log_file, 'r') as f:
    log_content = f.read()

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3",  # or your custom model name
    "prompt": f"Analyze this Jenkins CI/CD log:\n\n{log_content}",
    "stream": False
})

print("=== AI Analysis Output ===")
print(response.json().get("response", "No response"))
