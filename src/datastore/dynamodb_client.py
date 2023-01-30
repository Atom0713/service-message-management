import boto3

db = boto3.client("dynamodb", endpoint_url="http://localhost:8000")
