import pytest
import pandas as pd

@pytest.fixture
def data():
    df_data_test = pd.read_csv("mock.csv")
    return df_data_test