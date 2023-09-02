import sys

from app.app import handler, APP_VERSION


def test_handler():
    response = handler("", "")

    assert response.get("statusCode") == 200
    assert response.get("body") == f"Hello from lambda using docker: {sys.version}\nCurrent app version: {APP_VERSION}"
