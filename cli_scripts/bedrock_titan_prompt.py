import boto3
import json

client = boto3.client('bedrock-runtime')
prompt = input("Enter your prompt: ")
payload = { 
    "inputText": prompt,
    "textGenerationConfig": {
        "maxTokenCount": 4096,
        "stopSequences": [],
        "temperature": 0,
        "topP": 1
    }   
}

response = client.invoke_model(
    modelId ="amazon.titan-text-lite-v1",
    body = json.dumps(payload),
    accept = "application/json",
    contentType = "application/json"
)

print(response['body'].read().decode('utf-8'))
