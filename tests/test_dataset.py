import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src import create_dataset, utils
from pandas import DataFrame
import pytest

@pytest.fixture
def get_config():
    config = utils.open_yaml("params.yaml")
    return config

def test_data_preparation(get_config):
    df = create_dataset.create_ds("params.yaml")
    ds_path = get_config['data']["dataset_path"].split("/")[-1]

    assert type(df)== DataFrame
    assert (ds_path in os.listdir("data"))==True



