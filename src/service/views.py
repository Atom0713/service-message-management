from flask import Blueprint

bp = Blueprint("message", __name__)


@bp.route("/")
def hello():
    return {"status": "OK"}
