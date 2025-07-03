FROM python:3.10-slim

WORKDIR /app

COPY consumer.py .

RUN pip install --no-cache-dir kafka-python pandas

CMD ["python", "consumer.py"]