import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_est_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):

    # error handling
    if(Pregnancies == 0 and Glucose == 0 and BloodPressure == 0 and SkinThickness == 0 and Insulin == 0 and BMI == 0 and DiabetesPedigreeFunction == 0 and Age == 0):
        return [0]

    input1 = [Pregnancies]
    input2 = [Glucose]
    input3 = [BloodPressure]
    input4 = [SkinThickness]
    input5 = [Insulin]
    input6 = [BMI]
    input7 = [DiabetesPedigreeFunction]
    input8 = [Age]

    data = {
        "Pregnancies":input1,
        "Glucose":input2,
        "BloodPressure":input3,
        "SkinThickness":input4,
        "Insulin":input5,
        "BMI":input6,
        "DiabetesPedigreeFunction":input7,
        "Age":input8
    }
    data_set = pd.DataFrame(data)


    return (__model.predict(data_set))


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/diabetes_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()