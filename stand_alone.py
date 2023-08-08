import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def pred_score(location,sqft,bath,bhk):

    with open('static/home_prices_model.pickle','rb') as f:
        model = pickle.load(f)

    try:
        x = pd.read_csv("static/x_data.csv")
    except Exception as e:
        print("Error loading 'x_data.csv':", e)

    x = x.drop(x.columns[0],axis=1)
    
    #if (x.empty or (x.shape[1] == 0)):
        #return "Error: DataFrame 'x' is empty.  "
    
    #print("Column Names:", x.columns)
    #print(x.shape)
    
    x = list(x)
    #print(x)
    #loc_index1 = np.where(x.columns==location)[0][0]

    x = [element.lower() for element in x]

    #print(x)
    loc_index = x.index(location)
    #print(loc_index1)
    #print(loc_index)
    a = np.zeros((244))
    a[0] = sqft
    a[1] = bath
    a[2] = bhk
    if loc_index >= 0:                  # as we did one hot encoding the index with one will specify that it's the location
       a[loc_index] = 1
    return round(model.predict([a])[0],2)

print(pred_score('1st block jayanagar',1000,2,2))



