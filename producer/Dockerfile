FROM python:3.10-slim

WORKDIR /app

# Copy your Python script into the image
COPY producer.py .

# Install required packages
RUN pip install --no-cache-dir kafka-python pandas

# Command to run when the container starts
CMD ["python", "producer.py"]