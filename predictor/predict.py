import glob
import os
import joblib

from modelTraining.preprocessing import preprocess

def predict_car_price_using_pretrained_model(doUseLocalModel:bool, userInput_df):
    try:
        if doUseLocalModel:
            model = load_model_from_local()
            print("Model Loaded Successfully")

            #Added dummy output column before preprocessing.
            userInput_df['Price'] = 0
            print(f"User input dataframe: {userInput_df}")

            preprocessed_df = preprocess(userInput_df)

            #Removed dummy output column beforeprediction.
            preprocessed_df.drop('Price', axis=1, inplace=True)

            print(preprocessed_df)
            print(f"Preprocessed dataframe: {userInput_df}")

            prediction = model.predict(preprocessed_df)
            print(f"Prediction: {prediction}")
            return f"Predicted proise: {prediction[0]:.2f}"
        else:
            return "predicted car price is $100"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def load_model_from_local():

    search_path = os.path.join(".\models", "*_model_*.pkl")
    list_of_files = glob.glob(search_path)
    
    latest_file = max(list_of_files, key=os.path.getmtime)
    print(f"Loading model from latest updated file: {latest_file}")

    model = joblib.load(latest_file)
    return model
