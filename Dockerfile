FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr (critical for Docker logs)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first to leverage Docker layer caching
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Document the port the container listens on
EXPOSE 8080

# Start the production web server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
