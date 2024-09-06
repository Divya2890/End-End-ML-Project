## Creating a testing pipeline that takes a sample row as an input and uses the best_model.pkl file to 
## find the predicted total_score 
## before that, i have to create a flask applications that lets user give an input through a form
from Mlops.logger import logging
from Mlops.exceptions import Custom_Exception
from Mlops.utils import load_object
import os
import pandas as pd

class Predict_Pipeline():
    def __init__(self):
        pass
    def predict_sample(self, sample):
        best_model_path = os.path.join("artifacts","best_model.pkl")
        preproccesor_obj_path  = os.path.join("artifacts",'preprocessor.pkl')
        model = load_object(best_model_path)
        preproccesor_obj = load_object(preproccesor_obj_path)

        # first apply data preprocessing to the sample data and use the best model to predict the 
        # total score of the sample data
        print("PATHBKJFSN",preproccesor_obj)
        transf_data = preproccesor_obj.transform(sample)
        print("transf_data",transf_data)
        result = model.predict(transf_data)
        return result

class Custom_data:
        def __init__(self,gender: str,race_ethnicity: str,parental_level_of_education,
        lunch: str,test_preparation_course: str,  reading_score: int, writing_score: int ):

            self.gender = gender
            self.race_ethnicity = race_ethnicity
            self.parental_level_of_education = parental_level_of_education
            self.lunch = lunch
            self.test_preparation_course = test_preparation_course
            self.reading_score = reading_score
            self.writing_score = writing_score

        
        def convert_to_dataframe(self):
            print("Gender", self.gender,"luch", self.lunch)
            df = pd.DataFrame(columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score'])
            df['gender'] = [self.gender]
            df['race/ethnicity'] = [self.race_ethnicity]
            df['parental level of education'] = [self.parental_level_of_education]
            df['lunch'] = [self.lunch]
            df['test preparation course']  =  [self.test_preparation_course]
            df['reading score'] = [self.reading_score]
            df['writing score'] = [self.writing_score]
            return df
