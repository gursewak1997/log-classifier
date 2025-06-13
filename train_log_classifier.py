# train_log_classifier.py
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load data
df = pd.read_csv("data/logs.csv")
X, y = df["log"], df["label"]

# Define and train model
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/log_classifier.pkl")
print("✅ Model trained and saved to model/log_classifier.pkl")

