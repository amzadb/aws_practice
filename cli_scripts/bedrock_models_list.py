import boto3

client = boto3.client("bedrock")

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