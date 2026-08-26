import boto3

client = boto3.client("bedrock")

# Get all models
response = client.list_foundation_models()

# Extract unique providers
providers = {}
for model in response['modelSummaries']:
    provider_name = model['providerName']
    if provider_name not in providers:
        providers[provider_name] = []
    providers[provider_name].append(model)

# Display providers with numbers
print("\n=== Available Providers ===\n")
provider_list = sorted(list(providers.keys()))
for idx, provider in enumerate(provider_list, 1):
    print(f"{idx}. {provider}")

# Get user selection
print()
while True:
    try:
        selection = int(input("Select a provider by number: ").strip())
        if 1 <= selection <= len(provider_list):
            selected_provider = provider_list[selection - 1]
            break
        else:
            print(f"Please enter a number between 1 and {len(provider_list)}")
    except ValueError:
        print("Please enter a valid number")

# Display models for selected provider
print(f"\n=== Models from {selected_provider} ===\n")
models = providers[selected_provider]
for idx, model in enumerate(models, 1):
    print(f"{idx}. Model Id: {model['modelId']}")
    print(f"   Model Name: {model['modelName']}")
    print()