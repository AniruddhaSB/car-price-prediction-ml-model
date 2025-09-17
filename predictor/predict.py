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
            return f"Predicted price of a car: {prediction[0]:.2f}"
        else:
            return "predicted car price is $100"
    except Exception as e:
        return f"An unexpected error occurred: {e}"



def load_model_from_local():
    # Use forward slashes for cross-platform compatibility
    search_path = os.path.join("models", "*_model_*.pkl")
    print(f"Searching for models at: {search_path}")

    # Use a sorted list to get the first one alphabetically.
    list_of_files = sorted(glob.glob(search_path))

    # Add a check to see if any files were found.
    if not list_of_files:
        raise FileNotFoundError(f"No model files found matching the pattern '{search_path}'")

    lastest_file = list_of_files[-1]
    print(f"Found and loading the following model file: {lastest_file}")

    try:
        model = joblib.load(lastest_file)
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load the model file '{lastest_file}': {e}")
    
def load_model_from_local_old():

    search_path = os.path.join(".\models", "*_model_*.pkl")
    list_of_files = glob.glob(search_path)
    
    #Take the first one.
    sorted_files = sorted(list_of_files)
    first_file = sorted_files[0] 
    
    model = joblib.load(first_file)
    return model
