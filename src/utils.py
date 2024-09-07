## This file contains few of the most commonly used 
## user defined functions needed to implement the End-End ML project

import os
import sys
import pickle
from Mlops.exceptions import Custom_Exception

from sklearn.metrics import accuracy_score,r2_score
from sklearn.model_selection import GridSearchCV
import pandas as pd

def save_obj(file_path, obj ):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    pickle.dump(obj,open(file_path,'wb'))

def evaluate_models(x_train,x_test,y_train,y_test, models, parameters):
    accuracy = {}
    #print("xtrain",x_train.shape,x_train.columns,x_test.shape,x_test)
    try:
        for key,value in models.items():
            model = value
            print(parameters[key],"paramters")
            gs = GridSearchCV(estimator=model,param_grid=parameters[key],cv=3)
            print("GS")
            gs.fit(x_train,y_train)
            print("fit")
            best_parameters = gs.best_params_
            print("best parameters",best_parameters)
            model.set_params(**best_parameters)
            print("model,set_params")
            model.fit(x_train,y_train)
            print("model,fititng")
            predictions = model.predict(x_test)
            print("predict",predictions)
            accuracy[key] = r2_score(y_test,predictions)
            print("R2 score of model",key,accuracy[key] )

        return accuracy
    except Exception as e:
        print( Custom_Exception().custom_exception(e,sys))

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise Custom_Exception().custom_exception(e, sys)


    



