import botocore

from .dynamodb_client import db

TABLE_NAME = "dev-service-message-management"


def create_table():
    try:
        # Create the DynamoDB table.
        _ = db.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName": "pk", "KeyType": "HASH"}, {"AttributeName": "sk", "KeyType": "RANGE"}],
            AttributeDefinitions=[
                {"AttributeName": "pk", "AttributeType": "S"},
                {"AttributeName": "sk", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )

        # Wait until the table exists.
        waiter = db.get_waiter("table_not_exists")
        waiter.wait(TableName=TABLE_NAME)
    except botocore.exceptions.ClientError:
        print("Table already exists.")


def delete_table() -> None:
    try:
        db.delete_table(TableName=TABLE_NAME)
        return
    except botocore.exceptions.ResourceNotFoundException:
        pass
