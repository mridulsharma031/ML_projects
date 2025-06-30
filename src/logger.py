import os
import sys
from datetime import datetime
import logging

from src.exception import CustomException


LOG_FILE= f"{datetime.now().strftime('%d_%m_%Y__%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "%(asctime)s ---[%(levelname)s]-- %(message)s",
    level=logging.INFO
)


# below lines were used in order to test the functionality of the logger and exception files
'''
if __name__=="__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("divide by zero error")
        raise CustomException(e,sys)
'''