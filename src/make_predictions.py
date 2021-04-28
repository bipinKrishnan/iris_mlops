import numpy as np 

import joblib 
from utils import open_yaml

def make_prediction(config, inputs):
    config = open_yaml(config)
    #inputs = np.array([1.2, 3.4, 2.2, 1.6]).reshape(1, -1)
    model = joblib.load(config['model']['model_path'])
    preds = model.predict(inputs)
    return preds