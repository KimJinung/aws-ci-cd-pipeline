import sys


def handler(event, context):
    message = f"Hello from lambda using docker: {sys.version}"
    return {
        "statusCode": 200,
        "body": message
    }
