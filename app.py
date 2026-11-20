
import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load the model downloaded during the Docker image build
model = mlflow.pyfunc.load_model("model")

class PredictionInput(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: PredictionInput):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
