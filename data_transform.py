import pandas as pd
import sklearn

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


# Use custom pipelines or sklearn pipelines 


class DataPreprocesisng:
    
    def __init__(self, cat_values):
        self.cat_values = cat_values
     
    def fit(self, X):
        pass 
    
    def transform(self, X):
        pass 
        
    