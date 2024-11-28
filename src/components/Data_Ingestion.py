import pandas as pd
import os
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass
import sys
import numpy as np
from pymongo.mongo_client import MongoClient
from zipfile import Path
from constant import *

@dataclass 
class DataIngestionConfig:
    artifact_folder : str = os.path.join(artifact_folder)

class DataIngestion:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils
    
    def export_collection_as_dataframe(self, collection_name, db_name):
        try:
            mongoclient = MongoClient(MONGO_DB_URL)
            collection = mongoclient[db_name][collection_name]
            df = pd.DataFrame(collection.find())
            if "_id" in df.columns.to_list():
                df.drop("_id", inplace=True)
            df.replace("na", np.nan, inplace=True)
            return df
        except Exception as e:
            raise CustomException(e, sys)
        
    def export_data_into_feature_store_file_path(self) -> pd.DataFrame:
        try:
            logging.info("exporting data from mongodb")
            sensor_data = self.export_collection_as_dataframe(MONGO_COLLECTION_NAME, MONGO_DATABASE_NAME)
            raw_file_path =  self.data_ingestion_config.artifact_folder
            logging.info("saving exported data into feature store file path :{raw_file_path}")
            feature_file_path = os.path.join(raw_file_path, "wafer_fault")
            os.makedirs(feature_file_path, exist_ok=True)
            sensor_data.to_csv(feature_file_path, index=False)
            return feature_file_path
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self) -> Path:
        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()
            logging.info("got the data from mongodb")
            logging.info("exited initiate_data_ingestion methods of data ingestion class")
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)
        
