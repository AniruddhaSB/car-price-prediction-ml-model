from .preprocessing import load_data_from_csv

def build_model_using_local_data():

    #Load data
    df = load_data_from_csv("modelTraining\\data\\car_sales_data.csv")
    print(df.head(5))