import uuid
from datetime import datetime
from typing import Dict, List, Optional

import botocore

from ..datastore import TABLE_NAME, dynamodb_client


class Message:
    table_name = TABLE_NAME
    pk: str = "MESSAGE"
    sk: str
    message: str
    fetched: bool = False
    created_at: str
    updated_at: str = ""

    def __init__(self, email: str, message: str) -> None:
        self.message = message
        self.sk = f"{email}_{uuid.uuid4()}"

    def _before_save(self):
        self.created_at = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def save(self):
        self._before_save()
        return dynamodb_client.put_item(
            TableName=TABLE_NAME,
            Item={
                "pk": {"S": self.pk},
                "sk": {"S": self.sk},
                "message": {"S": self.message},
                "fetched": {"BOOL": self.fetched},
                "created_at": {"S": self.created_at},
                "updated_at": {"S": self.updated_at},
            },
            ReturnValues="NONE",
        )

    @staticmethod
    def delete(message_key: str) -> None:
        dynamodb_client.delete_item(
            TableName=TABLE_NAME,
            Key={
                "pk": {"S": Message.pk},
                "sk": {"S": message_key},
            },
        )

    @staticmethod
    def fetch_new(recipient_email: str) -> List[Optional[Dict]]:
        messages = dynamodb_client.query(
            TableName=TABLE_NAME,
            ConsistentRead=True,
            KeyConditionExpression="pk = :primarykeyvalue AND begins_with(sk, :sortkeyval)",
            FilterExpression="fetched = :current_state",
            ExpressionAttributeValues={
                ":current_state": {"BOOL": False},
                ":sortkeyval": {"S": recipient_email},
                ":primarykeyvalue": {"S": Message.pk},
            },
        )

        # Should be done in a transaction
        collect_new_messages = []
        for sk in [item["sk"]["S"] for item in messages["Items"]]:
            try:
                response = dynamodb_client.update_item(
                    TableName=TABLE_NAME,
                    Key={"pk": {"S": Message.pk}, "sk": {"S": sk}},
                    ReturnValues="ALL_NEW",
                    UpdateExpression="SET updated_at = :update_date, fetched = :new_state",
                    ConditionExpression="fetched = :current_state",
                    ExpressionAttributeValues={
                        ":new_state": {"BOOL": True},
                        ":current_state": {"BOOL": False},
                        ":update_date": {"S": datetime.now().strftime("/%Y/%m/%d, %H:%M:%S")},
                    },
                )
                collect_new_messages.append(response)
            except botocore.exceptions.ClientError:
                # if operation fails means message was already fetched
                pass

        return collect_new_messages

    @staticmethod
    def fetch_all(recipient_email: str, start: str, end: str) -> Dict:
        messages = dynamodb_client.query(
            TableName=TABLE_NAME,
            ConsistentRead=True,
            KeyConditionExpression="pk = :primarykeyvalue AND begins_with(sk, :sortkeyval)",
            ExpressionAttributeValues={
                ":sortkeyval": {"S": recipient_email},
                ":primarykeyvalue": {"S": Message.pk},
            },
        )

        return messages
