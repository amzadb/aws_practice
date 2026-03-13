"""
AWS Lambda function to list all S3 buckets in your AWS account using boto3.
Can be deployed as a Lambda or run locally for testing.
Returns bucket names in a JSON response.
"""
import boto3

def lambda_handler(event, context):
    try:
        s3 = boto3.client('s3')
        buckets = s3.list_buckets()

        names = [b['Name'] for b in buckets['Buckets']]

        return {
            "statusCode": 200,
            "buckets": names
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }

if __name__ == "__main__":
    # Local test: call lambda_handler with dummy event/context and print output
    result = lambda_handler({}, None)
    print(result)
