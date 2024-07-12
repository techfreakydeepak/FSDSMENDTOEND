
from src.DimondPricePrediction.components.data_ingestion import DataIngestion

import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException
import pandas as pd

obj=DataIngestion()
obj.initiate_data_ingestion()

#python -m src.DimondPricePrediction.pipelines.training_pipeline this command is used in bash with help of blackbox ai to created the
# pipeline and run the training pipeline and artifacts