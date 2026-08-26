import boto3
import json

client = boto3.client('bedrock-runtime', region_name='us-east-1')
prompt = input("Enter your prompt: ")

# Invoke Titan Embedding model
response = client.invoke_model(
    modelId='amazon.titan-tg1-large',
    body=json.dumps({
        'inputText': prompt
    })
)

result = json.loads(response['body'].read())
print(result)
 
