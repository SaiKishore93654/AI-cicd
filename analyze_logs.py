
import sys
import subprocess
import json

log_input = sys.stdin.read()

response = subprocess.run(
    ["ollama", "run", "llama3"],
    input=f"Analyze this Jenkins build log:\n\n{log_input}".encode(),
    capture_output=True
)

# If using stream output, handle JSON stream
for line in response.stdout.splitlines():
    try:
        obj = json.loads(line)
        print(obj.get("response", "").strip(), end='', flush=True)
    except json.JSONDecodeError:
        print(line.decode(), end='')
