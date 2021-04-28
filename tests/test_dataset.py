import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src import create_dataset
from pandas import DataFrame

def test_data_preparation():
    df = create_dataset.create_ds("params.yaml")

    assert type(df)== DataFrame



