from ..datastore import TABLE_NAME, dynamodb_client


class Recipient:
    table_name = TABLE_NAME
    pk: str = 'RECIPIENT'
    sk: str
    name: str
    email: str

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def _before_save(self):
        self.sk = self.email


    def save(self):
        self._before_save()
        return dynamodb_client.put_item(
            TableName=TABLE_NAME,
            Item={
                'pk': {'S': self.pk},
                'sk': {'S': self.sk},
                'name': {'S': self.name},
            }
        )
