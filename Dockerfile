ARG PYTHON_VERSION=3.9

# !Apple Silicon must use platform option!
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:$PYTHON_VERSION

COPY requirements.txt ${LAMBDA_TASK_ROOT}

COPY app/ ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

CMD ["app.handler"]