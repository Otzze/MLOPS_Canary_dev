# CANARY DEPLOYMENT EXAMPLE FOR MLFLOW HANDLED PREDICTION MODELS

## STARTUP

### 1. Start the MLflow Tracking Server

Run MLflow locally before starting the FastAPI service

```bash
mlflow server --host 0.0.0.0 --port 8080
```

### 2. Train and register the Model

```bash
python model.py
```

### 3. Build and run the FastAPI service

```bash
docker compose up --build
```

Once you see:

Loading model...
Model loaded.

The /predict endpoint can be used

### 4. Test the API

```bash
curl -X POST http://127.0.0.1:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"data": [[5.1, 3.5, 1.4, 0.2]]}'
```

Example response:

```bash
{
  "model_used": "current_model",
  "predictions": [0]
}
```

test_api.py can also used for testing if edited with the correct parameters
