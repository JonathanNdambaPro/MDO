import pandas as pd
import yaml
import os

def get_mock():
    with open('mock.yml') as f:
        config_test = yaml.load(f, Loader=yaml.FullLoader)

    path_mock = f'{os.getcwd()}' + f'{os.sep}' + f'{config_test["path_to_mock"]}'
    mock = pd.read_csv(path_mock)
    return mock

def detect_num():
    """
    Check if all columns are numeric
    :return: boolean
    """
    mock = get_mock()

    if type(mock) == pd.DataFrame:
        for col in mock.columns:
            if pd.to_numeric(mock[col], errors='coerce').notnull().all(): continue
            else: return False

        return True

    else:
        for index in mock.shape[0]:
            if pd.to_numeric(pd.Series(mock[index]), errors='coerce').notnull().all(): continue
            else: return False

        return True



def detect_NaN():
    """
    Check if any element is nan
    :return: boolean
    """
    mock = get_mock()

    if type(mock) == pd.DataFrame:
        if mock.isnull().values.any(): return False
        else: return True

    else:
        mock_pd = pd.DataFrame(mock)
        if mock_pd.isnull().values.any(): return False
        else: return True


if __name__ == "__main__":
    var = detect_num()
