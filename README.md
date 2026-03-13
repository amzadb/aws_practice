# AWS Practice Project

This project demonstrates working with AWS S3 using Python.

## Prerequisites
- Python installed on your system
- AWS account
- AWS CLI installed ([Install Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))

## Setting Up AWS Credentials

### 1. Get Your Access Key and Secret Key
- Log in to the [AWS Console](https://aws.amazon.com/console/).
- Navigate to **IAM** (Identity and Access Management).
- Create a new user or select an existing user.
- Attach the necessary permissions (e.g., `AmazonS3FullAccess`).
- Generate an **Access Key ID** and **Secret Access Key**.

### 2. Configure AWS CLI
Open your terminal and run:

```
aws configure
```

You will be prompted to enter:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region name** (e.g., `us-east-1`)
- **Default output format** (e.g., `json`)

This will create a credentials file at `~/.aws/credentials`.

## Project Structure

```
aws_practice/
├── cli_scripts/
│   ├── s3_buckets.py
│   └── s3_file_upload.py
├── lambdas/
│   ├── s3_buckets.py
│   └── s3_file_upload.py
├── requirements.txt
├── sample_file.txt
└── README.md
```

## Running the Python Programs

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the scripts:

- For CLI-based S3 operations:

	List all S3 buckets:
	```
	python cli_scripts/s3_buckets.py
	```

	Upload a file to S3:
	```
	python cli_scripts/s3_file_upload.py
	```

- For Lambda-style S3 operations (can be run locally for testing):

	List all S3 buckets:
	```
	python lambdas/s3_buckets.py
	```

	Test the S3 file upload event Lambda handler locally:
	```
	python lambdas/s3_file_upload.py
	```
	```

## Troubleshooting
- Ensure your AWS credentials are correctly configured.
- Make sure your user has the necessary permissions for S3 operations.
- If you encounter errors, check your region and credentials.

## Useful Links
- [AWS CLI Configuration Docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
