import os
import sys
from car.logger import logging
from car.exception import CustomException
import pandas as pd

from car.components.dataingestion import DataIngestion
from car.components.datatransformation import DataTransformation
from car.components.modeltrainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))