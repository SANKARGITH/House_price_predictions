import json
import pickle
import numpy as np
import math

__locations = None
__data_columns =None
__model = None
__length = 0

def get_locations():
    return __locations

def get_predicted_price(location,sqft,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
         loc_index = -1
    x = np.zeros(__length)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],3)

def load_utils():
    global __locations
    global __data_columns
    global __model
    global __length
    with open('./models_utils/columns.json','r') as json_file:
        __data_columns = json.load(json_file)['data_columns']
        __locations = __data_columns[3:]
        __length = len(__data_columns)
    with open('./models_utils/banglore_home_prices_model.pickle','rb') as json_file:
        __model = pickle.load(json_file)

if __name__ == '__main__':
    load_utils()
    print(__length)
    print(get_locations())
    print(get_predicted_price('1st phase jp nagar',1200,2,2))