import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def generate_ml_debug_report(summary: str) -> str:
    prompt = f"""
You are a senior machine learning engineer reviewing a model.

Below is a structured summary of model evaluation and error analysis.

Your task:
1. Explain why the model may be failing.
2. Identify risks in the current approach.
3. Suggest concrete next steps to improve the model.
4. Keep the explanation practical and engineering-focused.

Model Summary:
{summary}
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)

    return response.json().get("response", "").strip()