import pytest
import pandas as pd
from pathlib import Path

@pytest.fixture
def data():
    p = Path('.')
    names_csv = list(p.glob('test_data/*.csv'))
    name_mock = [w for w in names_csv if "mock" in str(w)][0]
    df_data_test = pd.read_csv(name_mock)
    return df_data_test