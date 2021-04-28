import sys, os
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src')
sys.path.append(src_path)

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



