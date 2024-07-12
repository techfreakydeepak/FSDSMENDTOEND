import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self, config: DataIngestionConfig = DataIngestionConfig()):
        self.config = config

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebook/data", "cubic_zirconia.csv")))
            logging.info("I have read dataset as a df")

            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
            data.to_csv(self.config.raw_data_path, index=False)
            logging.info("I have saved the raw dataset in artifact folder")

            logging.info("Here I have performed train test split")

            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train test split completed")
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            train_data.to_csv(self.config.train_data_path, index=False)
            os.makedirs(os.path.dirname(self.config.test_data_path), exist_ok=True)
            test_data.to_csv(self.config.test_data_path, index=False)

            logging.info("Data Ingestion part is completed")

        except Exception as e:
            logging.error("Exception occurred during data ingestion stage")
            raise CustomException(e, sys)