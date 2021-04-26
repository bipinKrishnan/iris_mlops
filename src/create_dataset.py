import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris
from typer import Option, run

from utils import open_yaml

def create_ds(config: str=Option(...)):
    config = open_yaml(config)
    X, y = load_iris(return_X_y=True)

    columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'target']
    data = np.concatenate((X, np.expand_dims(y, 1)), axis=1)
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(config['data']["dataset_path"])

if __name__=="__main__":
    run(create_ds)
