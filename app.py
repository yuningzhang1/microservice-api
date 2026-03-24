from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI(title="Text Classification API")

# Define the request format using Pydantic
class PredictRequest(BaseModel):
    text: str

# Root endpoint (to check if API is running)
@app.get("/")
def home():
    return {"message": "API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    """
    This endpoint receives a text input and returns a prediction.
    For assignment purposes, we return a simple placeholder result.
    """
    
    input_text = request.text

    # Simple placeholder prediction (no model required)
    prediction = "positive"

    return {
        "input_text": input_text,
        "prediction": prediction
    }
