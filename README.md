# Civil_Aviation_ML
This is for the predicting flight price and the aviation delay status for domestic routes in Australia
# Flight Prediction Web Application

This assignment encompasses full-stack web development for an AI application. Utilising React.js for the frontend and FastAPI for backend operations, a website that takes in user input to process in an AI model and displays insights visually and informatively is developed.


## Table of Contents
- [Project Overview](#introduction)
- [Features](#features)
- [Architecture](#features)
- [Running the Application](#features)
- [Folder Structure](#installation)
- [API Documentation](#features)
- [Technologies Used](#usage)
- [Future Enhancements](#conclusion)

# Project Overview
The **Flight Prediction Web Application** offers users the following features:

- **Predict Flight Delays**  
  Users can predict whether a flight will be delayed based on flight details and weather data.

- **Predict Flight Cost**  
  Estimate the cost of a flight between two airports by considering various relevant factors.

- **Interactive Data Visualization**  
  Visualize prediction results and historical data through interactive charts.

This application leverages machine learning models to deliver accurate predictions and provides a user-friendly interface for:
- **Entering Inputs**
- **Viewing Results**
- **Exploring Data**

Enjoy seamless data insights and improved travel planning with this powerful tool!

# Features

- **Flight Delay Prediction**  
  Predicts the likelihood of a flight delay based on factors such as departure/arrival ports, temperature, wind speed, and airline.

- **Flight Price Prediction**  
  Estimates the flight cost based on the selected route, weather conditions, and airline.

- **Data Visualization**  
  Displays prediction results and other insights through interactive charts and maps for better data interpretation.

- **Error Handling**  
  Provides feedback for invalid inputs to enhance the user experience and ensure accurate predictions.

This application integrates machine learning models for reliable predictions, with a user-friendly interface that simplifies data input, result viewing, and data exploration.

# Architecture
The application consists of:

- **Front-End (React.js)**  
  Collects user inputs, displays prediction results, and provides interactive data visualizations using libraries like D3.js and Plotly.js.

- **Back-End (FastAPI)**  
  Processes HTTP requests, manages data preprocessing, and interacts with the machine learning models to generate predictions.

- **Machine Learning Models**  
  Pre-trained models stored in `.pkl` files, used for predicting delays and prices based on the inputs.

- **Optional Database**  
  For storing prediction history and user data, allowing for expanded capabilities in future analyses.

# Running the Application
In the project directory you can run:
- **1. Navigate to Backend Directory**
```bash
cd backend
```
- **Start the FastAPI Server (in anaconda environment)**
```bash
uvicorn main:app --reload
```
The server will start at http://127.0.0.1:8000
- **2. Navigate to Frontend directory**
```bash
cd ../frontend
```
- **Start the React application **
```bash
npm start
```
The front-end will start at http://localhost:3000
- **3. Access the application**
Open the web browser and go to http://localhost:300 to use the application.




# Folder Structure
Here is the overview of the website:
```bash
├── backend
│   ├── data                      # (Optional) Data files for predictions or historical data
│   ├── model                     # Pre-trained models and transformers
│   │   ├── flight_delay_model.pkl
│   │   ├── flight_price_model.pkl
│   │   ├── column_transformers.pkl
│   │   ├── price_column_transformers.pkl
│   │   └── scaler.pkl
│   ├── main.py                   # Main FastAPI application
│   ├── predict_delay.py          # Prediction logic for flight delays
│   └── predict_price.py          # Prediction logic for flight prices
│
├── frontend
│   ├── public                    # Public assets
│   ├── src                       # Main source folder for React components
│   │   ├── components
│   │   │   ├── D3Chart.js        # Custom D3.js charts
│   │   │   └── Navbar.js         # Navigation bar component
│   │   ├── pages
│   │   │   ├── About.js          # About page
│   │   │   ├── Charts.js         # Visualization page for flight data
│   │   │   ├── Home.js           # Home page
│   │   │   ├── Predict_Delay.js  # Delay prediction page
│   │   │   └── Predict_Price.js  # Price prediction page
│   ├── App.js                    # Main React component
│   ├── App.css                   # Main React design
│   └── index.js                  # Application entry point

```
## API documentation
## Endpoints

### GET /
- **Description**: Root endpoint to verify if the back-end is running.

### POST /predict_delay
- **Description**: Receives flight and weather data to predict if a flight will be delayed.
- **Request Body**: JSON object containing flight and weather details.
```bash
{
  "Port1": "Melbourne",
  "Port2": "Sydney",
  "MinTemp": 20,
  "MaxTemp": 30,
  "WindGustSpeed": 50,
  "Airline": "Qantas"
}
```

### POST /predict_price
- **Description**: Receives flight and weather data to predict if a flight will be delayed.
- **Request Body**: JSON object containing flight and weather details.
```bash
{
  "Port1": "Melbourne",
  "Port2": "Sydney",
  "MinTemp": 30,
  "MaxTemp": 40,
  "WindGustSpeed": 50,
  "Value": 250,
  "Airline": "Qantas",
  "Departing_Port": "Melbourne",
  "Arriving_Port": "Sydney"
}
```
# Technologies Used
- **Front-End:** React.js, Axios, D3.js, Chart.js, Plotly.js
Back-End: FastAPI, Uvicorn
- **Machine Learning Models:** Scikit-Learn models (serialized with Pickle)

# Future Enhancements:
- **Database Integration:** Store prediction history to allow users to view previous predictions.
- **User Authentication:** Add user accounts for personalized prediction history and settings.
- **Enhanced Visualization:** Implement additional interactive visualizations for deeper data insights.

