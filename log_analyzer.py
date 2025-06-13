import subprocess

def extract_errors(log_text):
    lines = log_text.splitlines()
    errors = [line for line in lines if "error" in line.lower() or "failed" in line.lower()]
    return "\n".join(errors[-30:]) if errors else log_text

def run_local_llm(prompt):
    try:
        process = subprocess.Popen(
            ["C:\\Users\\saiki\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "mistral"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = process.communicate(input=prompt.encode())
        if process.returncode != 0:
            return f"LLM failed: {err.decode()}"
        return out.decode()
    except Exception as e:
        return f"LLM error: {str(e)}"
