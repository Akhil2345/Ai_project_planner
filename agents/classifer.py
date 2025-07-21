from transformers import pipeline
from langchain.agents import Tool

# Load HF sentiment classifier
classifier_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Tool wrapper function
def classify_sentiment(text: str) -> str:
    result = classifier_pipeline(text)[0]
    label = result['label']
    score = round(result['score'], 4)
    return f"Sentiment: {label}, Confidence: {score}"
