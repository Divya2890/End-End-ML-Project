## This file contains few of the most commonly used 
## user defined functions needed to implement the End-End ML project

import os
import sys
import pickle

def save_obj(file_path, obj ):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    pickle.dump(obj,open(file_path,'wb'))



