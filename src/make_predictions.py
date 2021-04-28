import numpy as np 

import joblib 
from utils import open_yaml

def make_prediction(config: str, inputs: list) -> np.array:
    """
    Makes the prediction for the input provided

    Args:
      config(str): path to configuration file
      inputs: input features

    Returns:
      preds(array): prediction made by the model
    """
    config = open_yaml(config)
    #inputs = np.array([1.2, 3.4, 2.2, 1.6]).reshape(1, -1)
    model = joblib.load(config['model']['model_path'])
    preds = model.predict(inputs)
    return preds