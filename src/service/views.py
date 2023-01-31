from typing import Dict

from flask import Blueprint, request

from .controller import batch_remove_message, remove_message, retrieve_new_messages, submit_message

bp = Blueprint("message", __name__)


@bp.route("/")
def hello():
    return {"status": "OK"}


@bp.route("/message/<string:recipient_email>", methods=["POST"])  # DONE
def create_message(recipient_email: str) -> Dict:
    return submit_message(recipient_email)


@bp.route("/message/<string:message_key>", methods=["DELETE"])  # DONE
def delete_message(message_key: str) -> Dict:
    return remove_message(message_key)


@bp.route("/messages/<string:recipient_email>", methods=["GET", "DELETE"])
def handle_batch_fetc_delete_messages(recipient_email: str) -> Dict:
    """
    Fetch new messages for specific recipient
    """
    if request.method == "DELETE":
        return batch_remove_message()
    return retrieve_new_messages(recipient_email)  # DONE
