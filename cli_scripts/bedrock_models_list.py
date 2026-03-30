import boto3

# Replace with your actual credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

client = boto3.client("bedrock", 
    region_name="us-east-1",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

response = client.list_foundation_models()

count = 0
provider_name = ""
for model in response['modelSummaries']:
    # print(model)
    count += 1
    if model['providerName'] != provider_name:
        provider_name = model['providerName']
        print(f"Provider Name: ", model['providerName'])
        count = 1
    print(f"{count}. Model Id: ", model['modelId'])
    print(f"   Model Name: ", model['modelName'])
    print(f"   Model Version: ", model['modelVersion'])
    print(f"   Model Type: ", model['modelType'])