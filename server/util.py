import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_est_prediction(age,no_sex_partners,first_sex_intercourse,no_pregnancies,smokes,smokes_year):

    # error handling
    if(age == 0 and no_sex_partners == 0 and  first_sex_intercourse == 0 and  no_pregnancies == 0 and smokes == 0 and  smokes_year == 0):
        return [0]

    input1 = [age]
    input2 = [no_sex_partners]
    input3 = [first_sex_intercourse]
    input4 = [no_pregnancies]
    input5 = [smokes]
    input6 = [smokes_year]

    data = {
        'Age' : input1,
        'Number of sexual partners' : input2,
        'First sexual intercourse' : input3,
        'Num of pregnancies' : input4,
        'Smokes' : input5,
        'Smokes (years)' : input6,
        'Smokes (packs/year)' : [0],
        'Hormonal Contraceptives' : [0],
        'Hormonal Contraceptives (years)' : [0],
        'IUD' : [0],
        'IUD (years)' : [0],
        'STDs' : [0],
        'STDs (number)' : [0],
        'STDs:condylomatosis' : [0],
        'STDs:cervical condylomatosis' : [0],
        'STDs:vaginal condylomatosis' : [0],
        'STDs:vulvo-perineal condylomatosis' : [0],
        'STDs:syphilis' : [0],
        'STDs:pelvic inflammatory disease' : [0],
        'STDs:genital herpes' : [0],
        'STDs:molluscum contagiosum' : [0],
        'STDs:AIDS' : [0],
        'STDs:HIV' : [0],
        'STDs:Hepatitis B' : [0],
        'STDs:HPV' : [0],
        'STDs: Number of diagnosis' : [0],
        'STDs: Time since first diagnosis' : [0],
        'STDs: Time since last diagnosis' : [0],
        'Dx:Cancer' : [0],
        'Dx:CIN' : [0],
        'Dx:HPV' : [0],
        'Dx' : [0],
        'Hinselmann' : [0],
        'Schiller' : [0],
        'Citology' : [0]
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
        with open('./artifacts/cervical_cancer_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()