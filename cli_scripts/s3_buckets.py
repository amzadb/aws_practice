"""
Script to list all S3 buckets in your AWS account using boto3 and AWS CLI credentials.
Run directly from CLI to print bucket names.
"""
import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

print("Buckets in your AWS account:\n")

for bucket in response['Buckets']:
    print(bucket['Name'])