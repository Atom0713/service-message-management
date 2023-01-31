from typing import Dict

from flask import abort, request

from ..models import Message


def submit_message(recipient_email: str) -> Dict:
    Message(recipient_email, request.get_data(as_text=True)).save()

    return {"status": "ok"}


def remove_message(message_key: str) -> Dict:

    Message.delete(message_key)

    return {"status": "ok"}


def batch_remove_message() -> Dict:
    request_json = request.get_json()
    if not request_json:
        abort(400, "Missing required attribute: message_keys.")
    message_keys = request_json["message_keys"]

    for message_key in message_keys:
        Message.delete(message_key)

    return {"status": "ok"}


def retrieve_new_messages(recipient_email: str) -> Dict:
    start, end = (request.args.get("start"), request.args.get("end"))
    if start and end:
        # fetch all messages without updating state to fetched=true
        messages = Message.fetch_all(recipient_email, start, end)
        return {
            "recipient": recipient_email,
            "messages": [message["message"]["S"] for message in messages.get("Items")],
        }

    # fetch new messages and updated state to fetched=true
    messages = Message.fetch_new(recipient_email)
    return {"recipient": recipient_email, "messages": [message["Attributes"]["message"]["S"] for message in messages]}
