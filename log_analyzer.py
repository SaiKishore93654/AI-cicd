import subprocess

def extract_errors(log_text):
    lines = log_text.splitlines()
    errors = [line for line in lines if "error" in line.lower() or "failed" in line.lower()]
    return "\n".join(errors[-30:]) if errors else log_text

def run_local_llm(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "mistral"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = process.communicate(input=prompt.encode())
    return out.decode()
