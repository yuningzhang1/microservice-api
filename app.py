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
