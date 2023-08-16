import os
from car.exception import CustomException
from car.utils import load_object
import pandas as pd
import sys

'''
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            # Ensure that the features are in the correct order and shape for prediction
            feature_order = ['present_price', 'kms_driven', 'owner', 'age', 'fuel_type_diesel', 'fuel_type_petrol',
                             'seller_type_individual', 'transmission_mannual']
            features = features[feature_order]

            # Apply preprocessor transformation
            data_scaled = preprocessor.transform(features)

            # Make predictions using the model
            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)
    '''

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)

            # Ensure that the features are in the correct order and shape for prediction
            feature_order = ['Present_Price', 'Kms_Driven', 'Owner', 'age', 'Fuel_Type',
                             'Seller_Type', 'Transmission']
            features = features[feature_order]


            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self, Present_Price, Kms_Driven, Owner, age, Fuel_Type, Seller_Type, Transmission):
        self.Present_Price = Present_Price
        self.Kms_Driven = Kms_Driven
        self.Owner = Owner
        self.age = age
        self.Fuel_Type = Fuel_Type
        self.Seller_Type = Seller_Type
        self.Transmission = Transmission

    def get_data_as_data_frame(self):
        try:
            # Create a dictionary with the features and their values
            custom_data_input_dict = {
                "Present_Price": [self.Present_Price],
                "Kms_Driven": [self.Kms_Driven],
                "Owner": [self.Owner],
                "age": [self.age],
                "Fuel_Type": [self.Fuel_Type],
                "Seller_Type": [self.Seller_Type],
                "Transmission": [self.Transmission]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
        




'''
import sys
import pandas as pd
from source.exception import CustomException
from source.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        present_price: str,
        kms_driven: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.kms_driven = kms_driven

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

'''
