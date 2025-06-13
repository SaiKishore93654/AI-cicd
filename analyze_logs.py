import sys
from log_analyzer import extract_errors, run_local_llm
import webbrowser

if len(sys.argv) != 2:
    print("Usage: python analyze_logs.py <log_file>")
    sys.exit(1)

log_file = sys.argv[1]

with open(log_file, 'r') as f:
    log_text = f.read()

errors = extract_errors(log_text)
prompt = f"You are a DevOps expert. This CI/CD log failed:\n{errors}\n\nWhat caused the issue and how to fix it?"

print("Build failed. Ollama says:")
result = run_local_llm(prompt)
print(result)

# Open dashboard after analysis
webbrowser.open("http://localhost:8501")
