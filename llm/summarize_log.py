import os
import requests
from dotenv import load_dotenv
from log_preprocessor import extract_relevant_log_sections

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_log_with_openrouter(log_text):
    prompt = f"""
You are an AI assistant analyzing a CI/CD pipeline failure.

Instructions:
1. Identify the most likely root cause.
2. Recommend the next action an engineer should take.
3. State if this seems intermittent (yes/no).

Log snippet:
{log_text}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-4",
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
        raw_log = f.read()

    relevant_log = extract_relevant_log_sections(raw_log)
    result = analyze_log_with_openrouter(relevant_log)
    print("\nLLM Analysis:\n", result)
