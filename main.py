import os
from dotenv import load_dotenv
import logging
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from contextlib import asynccontextmanager
from modules.model import IrisData

logging.basicConfig(level=logging.INFO)
load_dotenv()

CLASS_NAMES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

# ----------------------
# LOAD MODEL ON STARTUP
# ----------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    from modules.model import IrisModel
    app.state.model = IrisModel()
    app.state.model.load_model()
    logging.info("Model loaded successfully")
    yield

app = FastAPI(lifespan=lifespan)

# ----------------------
# SECURITY SETTINGS
# ----------------------
API_SECRET = os.getenv("mysecret")
API_KEY_NAME = "api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if api_key_header == API_SECRET:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )

# ----------------------
# PREDICTION ENDPOINT
# ----------------------
@app.post("/predict", tags=["Prediction"])
async def predict_iris(data: IrisData, api_key: str = Depends(get_api_key)):
    model = app.state.model
    prediction = model.predict(data)
    return {"prediction": CLASS_NAMES[prediction[0]]}

# ----------------------
# HEALTH CHECK ENDPOINT
# ----------------------
@app.get("/health", tags=["Health"])
def health_check():
    if app.state.model:
        return {"status": "healty", "model_loaded": True}
    return {"status": "unhealthy", "model_loaded": False}