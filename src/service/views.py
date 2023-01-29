from flask import Blueprint, request

bp = Blueprint("message", __name__)


@bp.route("/")
def hello():
    return {"status": "OK"}


@bp.route("/message/<string:recipient_email>", methods=["GET", "POST", "DELETE"])
def resolve_message(recipient_email: str):
    if request.method == "POST":
        return {"status": "ok"}
    if request.method == "DELETE":
        return {"status": "ok"}

    return {"message": "message"}


@bp.route("/messages", methods=["GET", "DELETE"])
def resolve_messages():
    if request.method == "DELETE":
        return {"status": "ok"}

    return [{"recipient": "me", "message": "message"}]
