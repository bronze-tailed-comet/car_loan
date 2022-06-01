import pandas as pd
from utils.files_utils import save_file, load_file

import utils.ml_pipeline_config as config

test_size = config.params["test_split_ratio"]

def extract_raw():
    
    df = pd.read_csv('https://october-data-exercises.s3.eu-west-1.amazonaws.com/datasets/car_loan_trainset.csv')
    
    save_file(df, 'df_raw')