import logging
import os
from datetime import datetime

file_name = f'{datetime.now().strftime("%d-%m-%y-%H-%M-%S")}.log'
# creating a directory to store the log files that have been generated in the project
file_path = os.path.join(os.curdir,"logs")
os.makedirs(file_path,exist_ok = True)
file = os.path.join(file_path,file_name)
logger = logging.basicConfig(filename=file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

## Test code to see if the loggers.py files is being executed correctly
# if __name__ == '__main__':
#     logging.info("Testing the log message")