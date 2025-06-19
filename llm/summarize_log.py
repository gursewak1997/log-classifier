# llm/summarize_log.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_log_with_openrouter(log_text):
    prompt = f"""
    Analyze this CI/CD failure log and answer:
    1. What is the likely cause?
    2. What should the engineer do next?
    3. Is this an intermittent issue? (yes/no)

    Log:
    {log_text}
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost",  # required for OpenRouter
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-4",  # or try "mistralai/mixtral-8x7b", "anthropic/claude-3-haiku", etc.
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    with open("llm/sample_log.txt") as f:
        log = f.read()
    result = analyze_log_with_openrouter(log)
    print("\n🧠 LLM Analysis:\n", result)
