import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from Mlops.exceptions import Custom_Exception
from Mlops.logger import logging
import os
import sys
from Mlops.utils import save_obj


# Target is to create a pickle file for saving the data after performing 
# transformations like imputing, scaling, one hot encoding, creating train and test x, y data

@dataclass
class DataTranformationConfig:
    preprocessor_path : str = os.path.join('artifacts','preprocessor.pkl')

class Data_Transformation():
    def __init__(self):
        self.datatransform_config = DataTranformationConfig()

    def create_tranformer_obj(self):
        try:
            logging.info("Started to create preprocess obj")
            numerical_columns = []
            categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']

            num_pipeline = Pipeline(
                steps = [
                    ('handle_missing_values',SimpleImputer(strategy='median')),
                    ('scaling', StandardScaler())
                    ]
            )  
            cat_pipeline = Pipeline(
                steps = [
                    ('handle_missing_values',SimpleImputer(strategy = "most_frequent")),
                    ('encoding',OneHotEncoder(drop='first'))
                    ]
            )
            
            
            preprocessor =ColumnTransformer(
                [
                ('num',num_pipeline,numerical_columns),
                ('cat',cat_pipeline,categorical_columns)
                ]
            )
            logging.info('sucessfully created preprocess obj')
            return preprocessor
        except Exception as e:
            Custom_Exception().custom_exception(e,sys)

    def initiate_transformation(self):
        try:
            logging.info('Started to fit and transform the pipelines into train and testing data')
            train_data = pd.read_csv('artifacts/train.csv')
            test_data = pd.read_csv('artifacts/test.csv')
            train_data['Total_score'] = train_data.apply(lambda row: np.sum([row['math score'],row['writing score'],row['reading score']]),axis = 1)
            test_data['Total_score'] = test_data.apply(lambda row: np.sum([row['math score'],row['writing score'],row['reading score']]),axis = 1)
            x_train= train_data.drop(columns=['Total_score','math score','reading score','writing score'], axis =1)
            x_test= test_data.drop(columns=['Total_score','math score','reading score','writing score'],axis =1 )
            y_train = train_data['Total_score']
            y_test = test_data['Total_score']
            preproc_obj = self.create_tranformer_obj()
            x_train_transf = preproc_obj.fit_transform(x_train).toarray()
            x_test_transf = preproc_obj.transform(x_test).toarray()
            y_train = np.array(y_train).reshape(-1, 1)
            y_test=np.array(y_test).reshape(-1, 1)
            train_transf=np.c_[x_train_transf,y_train]
            test_transf=np.c_[x_test_transf,y_test]

            # creating a pickle file to save the preprocessing object that lets us store all the transformations needed 
            save_obj(DataTranformationConfig().preprocessor_path, preproc_obj)
            logging.info('Sucessfully saved the preprocess obj into a pickle file')
            return [train_transf,test_transf,preproc_obj]
        except Exception as e:
            Custom_Exception().custom_exception(e,sys)

if __name__ == '__main__':
    obj = Data_Transformation()
    obj.initiate_transformation()
