## Log Classifier

A simple machine learning script to classify CI/CD pipeline failure logs and suggest actions — ideal for triaging `konflux` failures like timeouts, infra issues, or dependency fetch problems.

---

### Quick Start

```bash
# Step 1: Clone and enter the project
cd log-classifier/

# Step 2: Set up Python environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Train the model
python train_log_classifier.py

# Step 5: Predict with a sample log
python predict_log.py
```

---

### Sample Output

```bash
(venv) ➜  ai python train_log_classifier.py
✅ Model trained and saved to model/log_classifier.pkl

(venv) ➜  ai python predict_log.py
🧠 Predicted root cause: dependency_error
💡 Suggested action: Check `cachi2` or retry dependency fetch.
```

---

### Sample Logs Format

**`data/logs.csv`**

```csv
log,label
"Error: TimeoutError, please try again.","intermittent"
"Failed to fetch from cachi2","dependency_error"
"Build failed due to missing xyz","missing_dependency"
"disk quota exceeded","infra_issue"
"task prefetch-dependencies has the status Failed","dependency_error"
```

---

### 💡 Future Ideas

* Slack integration on MR failures
* GitLab bot to auto-comment with `/retest` for intermittent errors
* Use OpenAI to suggest improved summaries
* More fine-grained labels (e.g., `cache_issue`, `network_glitch`)

---
