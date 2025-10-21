import mlflow
import pandas as pd
import random
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

CANARY_PROBABILITY = 0.1

app = FastAPI()
print("Loading model...")
mlflow.set_tracking_uri("http://host.docker.internal:8080")
current_model = mlflow.pyfunc.load_model(f"models:/tracking-quickstart/1")
print("Model loaded.")

class InputData(BaseModel):
    data: List[List[float]]

@app.post("/predict")
def predict(data: InputData):
    if random.random() < CANARY_PROBABILITY and "next_model" in globals():
        return next_model.predict(pd.DataFrame(data.data)).tolist()
    else:
        return current_model.predict(pd.DataFrame(data.data)).tolist()

@app.post("/update-model")
def update_model():
    global current_model
    global next_model
    next_model = mlflow.pyfunc.load_model(f"models:/tracking-quickstart/latest")
    return {"status": "model updated"}

@app.post("/accept-next-model")
def accept_next_model():
    current_model = next_model
