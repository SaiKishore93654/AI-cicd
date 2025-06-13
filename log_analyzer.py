import subprocess

def extract_errors(log_text):
    lines = log_text.splitlines()
    return "\n".join([l for l in lines if "error" in l.lower() or "failed" in l.lower() or "exception" in l.lower()])

def run_local_llm(prompt):
    try:
        process = subprocess.Popen(
            ["ollama", "run", "mistral"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = process.communicate(input=prompt.encode(), timeout=60)
        if process.returncode != 0:
            return f" Ollama error: {err.decode()}"
        return out.decode().strip()
    except Exception as e:
        return f" LLM call failed: {str(e)}"
