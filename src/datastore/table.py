import boto3

# import botocore.exceptions import ResourceInUseException
import botocore

db = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")


def create_table():
    try:
        # Create the DynamoDB table.
        table = db.create_table(
            TableName="dev-service-message-management",
            KeySchema=[{"AttributeName": "pk", "KeyType": "HASH"}, {"AttributeName": "sk", "KeyType": "RANGE"}],
            AttributeDefinitions=[
                {"AttributeName": "pk", "AttributeType": "S"},
                {"AttributeName": "sk", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )

        # Wait until the table exists.
        table.wait_until_exists()
    except botocore.exceptions.ClientError:
        print("Table already exists.")
