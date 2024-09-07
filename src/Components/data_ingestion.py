import pandas as pd
import numpy as np
from Mlops.logger import logging
from Mlops.exceptions import Custom_Exception
import os
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

# Points to be noted while doing this 
# 1. How are we obtaining our training data, is it from an API, SQL server, local path, cloud etc.
# 2. where are we storing the data in our project folder 

@dataclass
class DataIngestionConfig:
    train_path: str = os.path.join('artifacts','train.csv')
    test_path: str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw_data.csv')

class Data_Ingestion():
    def __init__(self):
       self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Started to Initiate data ingestion")
        try:
            data = pd.read_csv(f"Notebooks/data/StudentsPerformance.csv")
            train, test = train_test_split(data,test_size=0.3, random_state = 42)
            # create directory for train, test and raw data 
            os.makedirs('artifacts',exist_ok=True)
            train.to_csv(self.ingestion_config.train_path,index=False, header = True)
            test.to_csv(self.ingestion_config.test_path,index=False, header = True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False, header = True)
            logging.info("Successfully saved the train, test and raw data in the artifact folder")
        except Exception as e:
            Custom_Exception().custom_exception(e,sys)

if __name__ == '__main__':
    obj = Data_Ingestion()
    obj.initiate_data_ingestion()

    


