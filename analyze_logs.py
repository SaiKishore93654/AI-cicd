import sys
import webbrowser
from log_analyzer import extract_errors, run_local_llm

if len(sys.argv) < 2:
    print(" Usage: python analyze_logs.py <log_file>")
    sys.exit(1)

log_file = sys.argv[1]
with open(log_file, "r", encoding="utf-8") as f:
    log_text = f.read()

# Save for dashboard
with open("jenkins_log.txt", "w", encoding="utf-8") as f:
    f.write(log_text)

# Run analysis
errors = extract_errors(log_text)

if not errors.strip():
    print(" Build successful. No issues found.")
else:
    prompt = f"You are a DevOps engineer. These errors occurred:\n\n{errors}\n\nHow do we fix them?"
    result = run_local_llm(prompt)
    print("Build failed. Ollama says:")
    print(result)

# Auto-open browser dashboard
print(" Opening browser tab for dashboard...")
webbrowser.open("http://localhost:8501")
