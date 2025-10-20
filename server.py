import mlflow
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
print("Loading model...")
mlflow.set_tracking_uri("http://127.0.0.1:8080")
model = mlflow.pyfunc.load_model(f"models:/tracking-quickstart/2")
print("Model loaded.")

class InputData(BaseModel):
    data: List[List[float]]

@app.post("/predict")
def predict(data: InputData):
    return model.predict(pd.DataFrame(data.data)).tolist()

@app.post("/update-model")
def updafte_model():
    global model
    model = mlflow.pyfunc.load_model(f"models:/tracking-quickstart/latest")
    return {"status": "model updated"}
