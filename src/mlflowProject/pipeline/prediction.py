import joblib
# import numpy as np
# import pandas as pd
from pathlib import Path


MODEL_PATH = "artifacts/model_trainer/model.joblib"

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path(MODEL_PATH))
    
    def predict(self, data):
        prediction = self.model.predict(data)
        
        return prediction