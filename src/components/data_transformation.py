import numpy as np
import pandas as pd
import os
import sys

# import the custom packages that we created for the logging and exception

from src.logger import logging
from src.exception import CustomException
from src.utility import save_object


from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


@dataclass
class DataTransformatioConfig:

    Data_transformation_file_path= os.path.join('artifacts','preprocessed_data.pkl')

class DataTransformation:

    def __init__(self):
        self.data_transform_config=DataTransformatioConfig()

    def get_data_transformation_obj(self):
        

        try:
            num_feature=["reading score","writing score"]
            cat_feature=["gender","race/ethnicity","parental level of education","lunch","test preparation course"]
            

            num_pipeline=Pipeline(

                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("standardscaler",StandardScaler())
                ]
            
            )

            cat_pipeline=Pipeline(

                steps=[
                    ("imputation",SimpleImputer(strategy="most_frequent")),
                    ("OneHotencoding",OneHotEncoder())
                    ]
                )
            

            logging.info("computing the column Transpose")

            preprocessing= ColumnTransformer(
                [
                    ("numrical_feature",num_pipeline,num_feature),
                    ("categorical_feature",cat_pipeline,cat_feature)

                ]
            )

            return preprocessing

        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):


        try:
            print(train_path,test_path)
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)

            preprocessing_obj=self.get_data_transformation_obj()

            target_column_name="math score"

            input_feature_train_df=train_data.drop(columns=[target_column_name], axis=1)
            target_feature_train_df=train_data[target_column_name]

            input_feature_test_df=test_data.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_data[target_column_name]


            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            #input_feature_test_arr=preprocessing_obj.fit_transform(input_feature_test_df)

            #target_feature_train_arr=preprocessing_obj.transform(target_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            Train_arr= np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr= np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            save_object(
                file_path=self.data_transform_config.Data_transformation_file_path,
                obj=preprocessing_obj
            )

            return (
                Train_arr,test_arr,
                self.data_transform_config.Data_transformation_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)



