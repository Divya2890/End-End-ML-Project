import os
import sys
import pandas as pd
from src.logger import logging
from src.exceptions import Custom_Exception
from src.utils import save_obj, evaluate_models
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
from sklearn.metrics import accuracy_score, r2_score, classification_report
from dataclasses import dataclass
from src.Components.data_transformation import Data_Transformation

@dataclass
class ModelTrainingConfig:
    model_obj_path : str = os.path.join('artifacts','model.pkl')
    acc_rep_path: str = os.path.join('artifacts', 'accuracy_report.csv')

class Model_Trainer:
    def __init__(self):
        self.model_path = ModelTrainingConfig().model_obj_path
        self.acc_rep_path = ModelTrainingConfig().acc_rep_path
    
    def initiate_model(self,train,test):
        print("Entered to initalise our models")
        models = {
            "Random Forest Regressor" : RandomForestRegressor(),
            "Decision Tree Regressor" : DecisionTreeRegressor(),
            "Gradient Boosting" :  GradientBoostingRegressor(),
            "Ada Boost" : AdaBoostRegressor(),
            "XG Boost" : XGBRegressor(),
            "Linear Regression" : LinearRegression(),
            }
        
        parameters = {
            "Linear Regression": {},
            "Decision Tree Regressor":{
                #'min_samples_split':[2,4,6,8],
                #'max_depth': [50,100,25,15],
                'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                #'splitter': ['best','random'],
            },
            "Random Forest Regressor":{
                'n_estimators': [8,16,32,64,128,256],
                
            },
            "Gradient Boosting":{

                #'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                #'criterion':['squared_error', 'friedman_mse'],
                #'max_features':['sqrt','log2'],
                'n_estimators': [8,16,32,64,128,256]

            },

            "Ada Boost":{
                'learning_rate':[.1,.01,0.5,.001],
                #'loss':['linear','square','exponential'],
                'n_estimators': [8,16,32,64,128,256]
            },

            "XG Boost":{
                'learning_rate':[.1,.01,.05,.001],
                'n_estimators': [8,16,32,64,128,256]
            }

        }
        try:
            # Train all the models using training data
            training_data = train
            testing_data = test
            
            x_train = training_data[:,:-1]
            y_train = training_data[:,-1]
            x_test = testing_data[:,:-1]
            y_test = testing_data[:,-1]
            print("f jkacsf sd",x_train.shape,y_train.shape,x_test.shape,y_test.shape)
            # Evaluate all our models and find the best model through
                # Predict students performance on the testing data
                # Get the accuracy of all models 
            
            accuracy_report  = evaluate_models(x_train,x_test,y_train,y_test,models, parameters)
            
            report = {key: [value] for key,value in accuracy_report.items()}
            df = pd.DataFrame(report)
            df.to_csv(self.acc_rep_path)
            print("successfully evaluated my models", accuracy_report)
            # find the best model using the report
            maxi=max(accuracy_report.values())
            for key,value in accuracy_report.items():
                if accuracy_report[key] == maxi:
                    best_model = key
                    break
            
            # Since we have identifies the best model, we have to create a pickle file to store the best model
            # parameters and hyper parameter 
            best_model_obj = models[best_model]
            
            # save the best model as a pickle file 

            model_path = os.path.join("artifacts",'best_model.pkl')
            save_obj(model_path, best_model_obj)


            # we are returning the predictions for our best model on x_test
            y_test_pred = models[best_model].predict(x_test) 
            test_r2_score = r2_score(y_test,y_test_pred)

            return test_r2_score
        except Exception as e:
            print(Custom_Exception().custom_exception(e,sys))
    
if __name__ == '__main__':
    data_transformation = Data_Transformation()
    train_arr,test_arr,_= data_transformation.initiate_transformation()
    print("train",train_arr.shape,"test",test_arr.shape)
    obj = Model_Trainer()
    result = obj.initiate_model(train_arr,test_arr)
    print("Final Results",result)
    
