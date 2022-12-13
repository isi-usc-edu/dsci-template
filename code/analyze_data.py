import pandas as pd


def analyze(data):
    '''
    Convert original data to a pandas data frame

    Args:
        data - python dictionary

    Returns:
        df - a pandas data frame
    '''

    df = pd.DataFrame(data, index=data.keys())

    return df
