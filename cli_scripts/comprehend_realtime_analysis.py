import json
import boto3

# 1. Initialize the Amazon Comprehend client
# Replace 'us-east-1' with your preferred AWS region
comprehend_client = boto3.client("comprehend", region_name="us-east-1")

# 2. Define the text you want to analyze
sample_text = (
    "I am absolutely thrilled with the new upgrade! "
    "Luis from the New York office helped me set it up on Tuesday."
)

def run_realtime_analysis(text):
    print("--- Starting Real-Time Analysis ---\n")

    # Detect Sentiment (Positive, Negative, Neutral, Mixed)
    sentiment_response = comprehend_client.detect_sentiment(
        Text=text, LanguageCode="en"
    )

    print(f"Overall Sentiment: {sentiment_response['Sentiment']}")
    print(
        f"Confidence Scores: {json.dumps(sentiment_response['SentimentScore'], indent=2)}"
    )
    print("\n-----------------------------------\n")

    # Detect Entities (People, Places, Dates, etc.)
    entities_response = comprehend_client.detect_entities(
        Text=text, LanguageCode="en"
    )

    print("Detected Entities:")
    for entity in entities_response["Entities"]:
        print(
            f"- {entity['Text']} ({entity['Type']}) | Confidence: {entity['Score']:.2f}"
        )


if __name__ == "__main__":
    run_realtime_analysis(sample_text)
