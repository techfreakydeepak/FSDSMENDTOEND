import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException
from dataclasses import dataclass
from src.DimondPricePrediction.utlis.utlis import save_object
from src.DimondPricePrediction.utlis.utlis import evaluate_model

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, X_train, y_train, X_test, y_test):
        try:
            logging.info("Splitting Dependent and Independent Variables from train and test data")

            models = {
                "LinearRegression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "ElasticNet": ElasticNet()
            }

            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n=========================================================================\n')
            logging.info(f"Model Report:{model_report}")

            # to get best model score from dictionary
            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            print(f"Best Model Found, Model Name:{best_model_name}, R2 Score:{best_model_score}")
            print('\n=========================================================================\n')
            logging.info(f"Best Model Found, Model Name:{best_model_name}, R2 Score:{best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info('Exception occurred at Model Training')
            raise CustomException(e, sys)