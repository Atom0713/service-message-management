from ..datastore import TABLE_NAME, dynamodb_client


class Message:
    table_name = TABLE_NAME
    pk: str = 'MESSAGE'
    sk: str # <email>_<uuid>
    message: str
    email: str

    def __init__(self, email: str, message: str) -> None:
        self.message = message
        self.email = email

    def _before_save(self):
        self.sk = f'{self.email}_{}'

    def save(self):
        self._before_save()
        return dynamodb_client.put_item(
            TableName=TABLE_NAME,
            Item={
                'pk': {'S': self.pk},
                'sk': {'S': self.sk},
                'message': {'S': self.message},
            }
        )
