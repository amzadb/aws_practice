"""
Script to upload a file to a specified S3 bucket using boto3.
Uploads 'sample_file.txt' to 'my-demo-buket-practice'.
Run directly from CLI to perform the upload.
"""
import boto3

s3 = boto3.client('s3')

bucket_name = "my-demo-buket-practice"
file_name = "sample_file.txt"

s3.upload_file(file_name, bucket_name, file_name)
print("File uploaded successfully!")