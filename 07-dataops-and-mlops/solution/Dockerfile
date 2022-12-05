FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY api/ api
COPY modules/ modules

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]