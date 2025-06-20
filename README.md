# Log Failure Analyzer (LLM-Powered)

This project analyzes CI/CD pipeline failure logs using a Large Language Model (LLM) via the [OpenRouter API](https://openrouter.ai/). It extracts relevant error sections, sends them to an LLM, and returns root cause analysis, suggested actions, and intermittency detection.

## Features

- **LLM-powered root cause analysis** via OpenRouter (GPT-4, Claude, etc.)
- **Smart log preprocessing**: extracts only relevant log sections (e.g. failed tasks, tracebacks)
- Detects **intermittent issues** (timeouts, flaky tests)
- Recommends next steps (e.g., `/retest`)
- Easily extendable: Slack notifications, GitHub bots, JSON outputs, etc.

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

4. Add your OpenRouter API key to `.env`:

```bash
echo "OPENROUTER_API_KEY=your-openrouter-key" > .env
```

Replace `your-openrouter-key` with your actual OpenRouter API key.

## Folder Structure

```
log-classifier/
├── llm/
│   ├── summarize_log.py        # Sends relevant log summary to LLM
│   ├── log_preprocessor.py     # Extracts key sections from raw logs
│   └── sample_log.txt          # Example log to analyze
├── requirements.txt
├── .env                        # API key (ignored by Git)
└── README.md
```

## Usage

1. Add your CI log contents to `llm/sample_log.txt`.

2. Run the analyzer:

```bash
python llm/summarize_log.py
```

3. The output will include:

* Likely root cause
* Recommended action
* Whether the issue is intermittent

### Example Output

```
LLM Analysis:
1. Likely cause: Timeout while fetching dependencies from cachi2.
2. Suggested action: Retry using the `/retest` command.
3. Intermittent: yes
```

## Roadmap

* Slack notifications for failed jobs
* Konflux pipeline integration
* GitHub comment bot support
* JSON output for automation
* Prompt engineering & few-shot examples
* LLM caching for repeated runs

