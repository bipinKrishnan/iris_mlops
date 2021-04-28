import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris
from typer import Option, run
import sys
from utils import open_yaml

def create_ds(config: str=Option(...)) -> pd.DataFrame:
    """
    Prepares the Iris data and stores it as a csv file

    Args:
      config(str): path to configuration file containing
                   all parameters

    Returns:
      df(DataFrame): Iris data as a dataframe 
    """
    config = open_yaml(config)
    X, y = load_iris(return_X_y=True)

    columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'target']
    data = np.concatenate((X, np.expand_dims(y, 1).astype(int)), axis=1)
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(config['data']["dataset_path"], index=False)

    return df

if __name__=="__main__":
    run(create_ds)
