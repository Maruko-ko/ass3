import joblib
import pandas as pd

# Load the Random Forest Regressor model and transformers
price_model = joblib.load('model/flight_price_model.pkl')  
column_transformer = joblib.load('model/price_column_transformers.pkl')  

def predict_price(data):

    df = pd.DataFrame([data])
    processed_data = column_transformer.transform(df)
    prediction = price_model.predict(processed_data)
    return prediction[0]
