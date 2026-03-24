from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Text Classifier API")

# Request format
class PredictRequest(BaseModel):
    text: str

# Root endpoint
@app.get("/")
def root():
    return {"message": "API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(req: PredictRequest):
    # fake prediction (for assignment)
    return {
        "input_text": req.text,
        "prediction": "positive"
    }
from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.joblib")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    prediction = model.predict([text])[0]
    return {"prediction": str(prediction)}
