import pandas as pd
import os.path

def save_file(df, name):
    '''
    accepts dataframe list as input
    saves each dataframe in the tmp folder as csv
    the file name corresponds to the dataframe "name" attribute
    '''
    df.to_csv('/opt/airflow/data/' + name + '.csv' , sep=',', index=False)


def load_file(name):
    '''
    accepts a list of names (str) as input
    load each csv file from the tmp folder with the input names
    returns a list of loaded dataframes
    '''
    df = pd.read_csv("/opt/airflow/data/" + name + ".csv")
    return df