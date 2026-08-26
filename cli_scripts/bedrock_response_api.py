import boto3
import json
from dotenv import load_dotenv

load_dotenv()

client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "openai.gpt-oss-safeguard-20b"

# Prepare the request payload
prompt = "Can you explain the features of Amazon Bedrock?"

# Create the request body (OpenAI models use messages array format)
request_body = json.dumps({
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 500,
    "temperature": 0.7
})

# Invoke the model
response = client.invoke_model(
    modelId=model_id,
    body=request_body,
    contentType="application/json",
    accept="*/*"
)

# Parse the response
response_body = json.loads(response["body"].read().decode("utf-8"))
print(response_body) 