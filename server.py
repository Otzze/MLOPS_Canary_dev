import mlflow
from fastapi import FastAPI

app = FastAPI()

model = mlflow.pyfunc.load_model("models://iris_model")

@app.post("/predict")
def predict(data: dict):
    return model.predict(data)

@app.post("/update-model")
def updafte_model():
    global model
    model = mlflow.pyfunc.load_model("models://iris_model")
    return {"status": "model updated"}
