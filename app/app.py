import sys

APP_VERSION = "1.0.0"

def handler(event, context):
    message = f"Hello from lambda using docker: {sys.version} '\nCurrent app version: {APP_VERSION}"
    return {
        "statusCode": 200,
        "body": message
    }
