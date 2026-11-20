
import os
import mlflow
from mlflow.tracking import MlflowClient

# Connect to DagsHub
mlflow.set_tracking_uri(
    "https://dagshub.com/zahraatarhini7/mlflow-fastapi-deployment.mlflow"
)

# Find the latest registered model version
client = MlflowClient()

versions = client.search_model_versions(
    "name='RandomForestModel'"
)

if not versions:
    raise Exception("No registered model versions found!")

latest_version = max(versions, key=lambda v: int(v.version))

model_uri = f"models:/RandomForestModel/{latest_version.version}"

print(f"Downloading model version {latest_version.version}...")

# Download the model into the local model folder
mlflow.artifacts.download_artifacts(
    artifact_uri=model_uri,
    dst_path="model"
)

print("Model downloaded successfully!")
