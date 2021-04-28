import pandas as pd 
from sklearn.svm import SVC

import joblib
from typer import Option, run
from utils import open_yaml

def train_model(config: str=Option(...)):
    config = open_yaml(config)

    df = pd.read_csv(config['data']['dataset_path'])
    X, y = df.drop('target', axis=1).values, df['target'].values

    model = SVC()
    model.fit(X, y)
    acc = model.score(X, y)

    joblib.dump(model, config['model']['model_path'])

if __name__=="__main__":
    run(train_model)



