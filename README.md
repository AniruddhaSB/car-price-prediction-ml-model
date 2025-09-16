# Purpose
This project is to create a end to end working demo for machine learning with google cloud.

This dataset contains detailed information on car sales, covering multiple manufacturers and models. It is suitable for data analysis. 

Here we use it for price prediction

# Workflow
1. Raw data file is added in data folder.
2. Flask server endpoint /build_model_locally is used to build a new model.
3. Newly built model is preserved in models folder (with file name having the current timestamp)
4. Flask server endpoint /predict_local is used to predict the price of a car using locally trained model.
5. It will always use the latest model from /models folder during /predict_local.
6. /predict_local is a HTTP Get Endpoint. It exppect user inputs as query string for  prediction. 
Sample input -
/predict_local?Engine%20size=1.2&Year%20of%20manufacture=2012&Mileage=73470&Model=Polo&Fuel%20type=Petrol

# References
Details regarding Exploratory Data Analysis can be found here: https://www.kaggle.com/code/shmagibokuchava7/pricepredict-pro

# Dataset
https://www.kaggle.com/datasets/msnbehdani/mock-dataset-of-second-hand-car-sales
