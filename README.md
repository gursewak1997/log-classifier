# Log Failure Classifier (LLM-Powered)

This project analyzes CI/CD failure logs using a Large Language Model (LLM) via the [OpenRouter API](https://openrouter.ai/). It provides root cause analysis and actionable suggestions based on log contents.

## Features

- Summarizes and classifies log failures using LLMs (e.g., GPT-4 via OpenRouter)
- Detects intermittent issues
- Suggests next steps (e.g., rerun with `/retest`)
- Easily extendable for Slack notifications or CI integrations

## Setup

1. Clone the repository:

```bash
git clone https://github.com/gursewak1997/log-classifier.git
cd log-classifier
````

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your `.env` file:

```bash
echo "OPENROUTER_API_KEY=your-openrouter-key" > .env
```

Replace `your-openrouter-key` with your real OpenRouter API key.

## Folder Structure

```
log-classifier/
├── llm/
│   ├── summarize_log.py        # Main LLM-based log analyzer
│   └── sample_log.txt          # Sample input log file
├── requirements.txt
├── .env                        # Your OpenRouter API key (ignored by Git)
└── README.md
```

## Usage

Add your failure log content to `llm/sample_log.txt`, then run:

```bash
python llm/summarize_log.py
```

The script will print out the likely root cause, recommended actions, and whether the issue is intermittent.

## Example Output

```
LLM Analysis:
1. Likely cause: Dependency fetch timeout from cachi2.
2. Suggested action: Retry the run using the `/retest` command.
3. Intermittent: yes
```

## Roadmap

* Add Slack notifications
* Support structured JSON output
* Multi-task summarization
* GitHub comment bot integration

```
