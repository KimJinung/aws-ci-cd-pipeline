import sys, json

from app.app import handler


def test_handler():
    response = handler("", "")

    assert response.get("statusCode") == 200
    assert response.get("body") == f"Hello from lambda using docker: {sys.version}"