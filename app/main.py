from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np
import os

app = FastAPI()

# Setup for templates and static files
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load model
model_path = "app/model/risk_model.pkl"
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    model = None

# Root route: serves HTML page
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction endpoint
@app.post("/predict")
async def predict(data: dict):
    if model is None:
        return JSONResponse(content={"error": "Model not loaded"}, status_code=500)
    
    try:
        # Map categorical fields to numerical values
        change_type_map = {
            "feature": 0,
            "bugfix": 1,
            "hotfix": 2,
            "refactor": 3,
            "config": 4
        }
        time_map = {
            "morning": 0,
            "afternoon": 1,
            "evening": 2,
            "night": 3
        }

        # Format input as numpy array
        X = np.array([[
            int(data["files_changed"]),
            int(data["test_coverage"]),
            int(data["dependencies"]),
            int(data["previous_failures"]),
            change_type_map.get(data["change_type"], 0),
            time_map.get(data["deployment_time"], 0)
        ]])

        # Model prediction: probability of rollback
        risk_score = float(model.predict_proba(X)[0][1])

        # Risk interpretation
        if risk_score > 0.8:
            decision = "Block Deployment"
            status = "block"
        elif risk_score > 0.6:
            decision = "Rollback Required"
            status = "rollback"
        elif risk_score > 0.4:
            decision = "Monitor Closely"
            status = "monitor"
        else:
            decision = "Safe to Deploy"
            status = "proceed"

        # Return prediction + metadata
        response = {
            "risk_score": round(risk_score, 3),
            "latency": f"{int(200 + risk_score * 500)}ms",
            "error_rate": round(risk_score * 0.05, 3),
            "anomaly": "Detected" if risk_score > 0.6 else "Normal",
            "final_decision": decision,
            "status": status
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
