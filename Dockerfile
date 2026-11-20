
# syntax=docker/dockerfile:1.7

FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py fetch_model.py ./

# Fetch the latest registered model from DagsHub
RUN --mount=type=secret,id=dagshub_token,required=true \
    MLFLOW_TRACKING_USERNAME=zahraatarhini7 \
    MLFLOW_TRACKING_PASSWORD="$(cat /run/secrets/dagshub_token)" \
    python fetch_model.py

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
