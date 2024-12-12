from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predict_price import predict_price
from predict_delay import predict_delay
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models for the POST endpoints
class PricePredictionRequest(BaseModel):
    Port1: str
    Port2: str
    MinTemp: float
    MaxTemp: float
    WindGustSpeed: float
    Value: float
    Airline: str
    Departing_Port: str
    Arriving_Port: str

class PricePredictionResponse(BaseModel):
    Predicted_Price: float

class DelayPredictionRequest(BaseModel):
    Port1: str
    Port2: str
    MinTemp: float
    MaxTemp: float
    WindGustSpeed: float
    Airline: str

# POST Endpoint for flight price prediction
@app.post("/predict_price", response_model=PricePredictionResponse)
def get_price_prediction(request: PricePredictionRequest):
    data = request.dict()
    data["$Value"] = data.pop("Value")  # Convert 'Value' to '$Value' if necessary

    try:
        prediction = predict_price(data)
        return {"Predicted_Price": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in price prediction: {e}")

# GET Endpoint for flight price prediction (optional if needed for testing)
@app.get("/predict_price", response_model=PricePredictionResponse)
def get_price_prediction_get(
    Port1: str,
    Port2: str,
    MinTemp: float,
    MaxTemp: float,
    WindGustSpeed: float,
    Value: float,
    Airline: str,
    Departing_Port: str,
    Arriving_Port: str
):
    data = {
        "Port1": Port1,
        "Port2": Port2,
        "MinTemp": MinTemp,
        "MaxTemp": MaxTemp,
        "WindGustSpeed": WindGustSpeed,
        "$Value": Value,  # Rename to match the expected format
        "Airline": Airline,
        "Departing_Port": Departing_Port,
        "Arriving_Port": Arriving_Port
    }

    try:
        prediction = predict_price(data)
        return {"Predicted_Price": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in price prediction: {e}")

# POST Endpoint for flight delay prediction
@app.post("/predict_delay")
def get_delay_prediction(request: DelayPredictionRequest):
    data = request.dict()
    try:
        prediction = predict_delay(data)
        return {"Delay Prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in delay prediction: {e}")

# GET Endpoint for flight delay prediction
@app.get("/predict_delay")
def get_delay_prediction_get(
    Port1: str,
    Port2: str,
    MinTemp: float,
    MaxTemp: float,
    WindGustSpeed: float,
    Airline: str
):
    data = {
        "Port1": Port1,
        "Port2": Port2,
        "MinTemp": MinTemp,
        "MaxTemp": MaxTemp,
        "WindGustSpeed": WindGustSpeed,
        "Airline": Airline
    }

    try:
        prediction = predict_delay(data)
        return {"Delay Prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in delay prediction: {e}")