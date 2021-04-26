import pandas as pd 
from sklearn.svm import SVC

import mlflow

import joblib
from typer import Option, run
from urllib.parse import urlparse

from utils import open_yaml

def mlflow_log(config: str=Option(...)):
    config = open_yaml(config)
    
    mlflow.set_tracking_uri(config['mlflow']['tracking_uri'])
    mlflow.set_experiment(config['mlflow']['exp_name'])

    df = pd.read_csv(config['data']['dataset_path'])
    X, y = df.drop('target', axis=1).values, df['target'].values

    with mlflow.start_run(run_name=config['mlflow']['run_name']):
        model = SVC()
        model.fit(X, y)
        acc = model.score(X, y)

        mlflow.log_params({"C": model.C, "kernel": model.kernel})
        mlflow.log_metric("accuracy", acc)

        tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme
        mlflow.sklearn.log_model(model, "model")

if __name__=="__main__":
    run(mlflow_log)



