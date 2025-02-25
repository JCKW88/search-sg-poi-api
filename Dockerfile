ARG PYTHON_VERSION=3.13.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
