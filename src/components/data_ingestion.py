import numpy as np
import pandas as pd

import os 
import sys
from dataclasses import dataclass
#from logger import logging
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    
    train_data_path :str =os.path.join('artifacts','train.csv')
    test_data_path: str= os.path.join('artifacts','test.csv')
    raw_data_path: str= os.path.join('artifacts','raw_data.csv')
    



class DataIngestion:

    def __init__(self):
        self.DataIngestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        
        logging.info("data igenting started")



        try:
            df= pd.read_csv("notebook\data\StudentsPerformance.csv")

            os.makedirs(os.path.dirname(self.DataIngestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.DataIngestion_config.raw_data_path,index=False,header=True)

            logging.info("raw data is being ingestedted, starting with the train test split")

            train_set,test_set =train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.DataIngestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.DataIngestion_config.test_data_path,index=False,header=True)

            logging.info("data has been loaded successfully")
            
            return (

                self.DataIngestion_config.train_data_path,
                self.DataIngestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
    