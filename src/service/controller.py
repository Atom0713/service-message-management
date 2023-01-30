from typing import Dict

from flask import request

from ..models import Message


def submit_message(recipient_email: str) -> Dict:
    Message(recipient_email, request.get_data(as_text=True)).save()

    return {"status": "ok"}


def remove_message(message_key: str) -> Dict:

    Message.delete(message_key)

    return {"status": "ok"}


def batch_remove_message() -> Dict:
    message_keys = request.get_json()["message_keys"]

    for message_key in message_keys:
        Message.delete(message_key)

    return {"status": "ok"}


def retrieve_new_messages(recipient_email: str) -> Dict:
    start, end = (request.args.get("start"), request.args.get("end"))
    messages = Message.fetch_new(recipient_email, start, end)
    return {"recipient": recipient_email, "messages": [message["Attributes"]["message"]["S"] for message in messages]}
