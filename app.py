from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# request format
class PredictRequest(BaseModel):
    text: str

# root endpoint
@app.get("/")
def root():
    return {"message": "API is running"}

# predict endpoint
@app.post("/predict")
def predict(req: PredictRequest):
    return {
        "input_text": req.text,
        "prediction": "positive"
    }
