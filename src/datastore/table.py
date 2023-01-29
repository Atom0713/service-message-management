import botocore
from .dynamodb_client import db

TABLE_NAME = "dev-service-message-management"

def create_table():
    try:
        # Create the DynamoDB table.
        table = db.create_table(
            TableName=TABLE_NAME,
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
