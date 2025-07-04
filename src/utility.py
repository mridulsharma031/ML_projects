import os
import sys

from src.exception import CustomException
from src.logger import log_path
import dill




def save_object(file_path, obj):

    try:
        dir_name=os.path.dirname(file_path)

        os.makedirs(dir_name,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        CustomException(e,sys)
