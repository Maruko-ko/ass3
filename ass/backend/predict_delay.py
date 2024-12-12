import joblib
import pandas as pd

# Load the Random Forest model and transformers
delay_model = joblib.load('model/flight_delay_model.pkl')
column_transformer = joblib.load('model/column_transformers.pkl')
scaler = joblib.load('model/scaler.pkl')

def predict_delay(data):
    # Convert input data to DataFrame
    df = pd.DataFrame([data])
    # Transform and scale data
    processed_data = column_transformer.transform(df)
    processed_data = scaler.transform(processed_data)
    # Predict delay
    prediction = delay_model.predict(processed_data)
    return 'Delayed' if prediction[0] == 1 else 'Not Delayed'
