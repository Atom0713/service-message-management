import pytest


@pytest.mark.parametrize(
    "request_method, expected_response_json",
    [("GET", {"message": "message"}), ("POST", {"status": "ok"}), ("DELETE", {"status": "ok"})],
)
def test_resolve_message(request_method, expected_response_json, client):
    if request_method == "POST":
        response = client.post("/message/me")
    elif request_method == "DELETE":
        response = client.delete("/message/me")
    else:
        response = client.get("/message/me")

    assert response.status_code == 200
    assert response.get_json() == expected_response_json


@pytest.mark.parametrize(
    "request_method, expected_response_json",
    [("GET", [{"recipient": "me", "message": "message"}]), ("DELETE", {"status": "ok"})],
)
def test_resolve_messages(request_method, expected_response_json, client):
    if request_method == "DELETE":
        response = client.delete("/messages")
    else:
        response = client.get("/messages")

    assert response.status_code == 200
    assert response.get_json() == expected_response_json
