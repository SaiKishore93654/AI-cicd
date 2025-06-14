import subprocess

def extract_errors(log_text):
    lines = log_text.splitlines()
    errors = [line for line in lines if "error" in line.lower() or "failed" in line.lower()]
    return "\n".join(errors[-30:]) if errors else log_text

def build_prompt(log_text):
    context = (
        "You are an expert DevOps assistant helping debug CI/CD pipeline failures. "
        "This project is a Python application using pip and a requirements.txt file for dependency management. "
        "Only give suggestions relevant to Python and pip. Do not mention other platforms like Java (Maven) or JavaScript (npm).\n\n"
        "Here are the recent CI/CD log errors:\n\n"
    )
    return context + extract_errors(log_text)

def run_local_llm(log_text):
    prompt = build_prompt(log_text)
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
