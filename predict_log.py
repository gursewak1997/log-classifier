# predict_log.py
import joblib

log = """task prefetch-dependencies has the status "Failed":
Error: TimeoutError, please try again. If the issue seems to be on cachi2 side, contact the maintainers."""

# Load model
model = joblib.load("model/log_classifier.pkl")
label = model.predict([log])[0]

# Simple actions based on label
actions = {
    "intermittent": "Try rerunning with `/retest`.",
    "dependency_error": "Check `cachi2` or retry dependency fetch.",
    "missing_dependency": "Check if a required package is missing.",
    "infra_issue": "Disk/memory issue — ping infra team."
}

print(f"🧠 Predicted root cause: {label}")
print(f"💡 Suggested action: {actions.get(label, 'Review manually.')}")

