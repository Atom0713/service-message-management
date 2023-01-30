from .table import create_table, TABLE_NAME
from .dynamodb_client import db as dynamodb_client

__all__ = [
    "create_table",
    "TABLE_NAME",
    "dynamodb_client"
    ]


def seed_database():
    pass
