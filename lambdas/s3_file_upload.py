"""
AWS Lambda function to process S3 file upload events.
Prints the uploaded file name and bucket from the event records.
Returns a success message.
"""
import json

def lambda_handler(event, context):

    for record in event['Records']:

        bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']

        print("File uploaded:", file_name)
        print("Bucket:", bucket)

    return {
        "statusCode": 200,
        "message": "File upload event processed successfully!"
    }


if __name__ == "__main__":
    # Example event for local testing
    test_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": "example-bucket"},
                    "object": {"key": "example-file.txt"}
                }
            }
        ]
    }
    result = lambda_handler(test_event, None)
    print("Lambda handler result:", result)