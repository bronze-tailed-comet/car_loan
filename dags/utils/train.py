import pandas as pd
from datetime import datetime
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression

from utils.files_utils import load_file

import utils.ml_pipeline_config as config

def train():
    
    df = load_file('df_raw')

    features = config.params['features']

    target = config.params['target']

    xtrain, xtest, ytrain, ytest = train_test_split(df[features], df[target], test_size=config.params['test_split_ratio'],
                                                    stratify=df[target], random_state=0)

    model = LogisticRegression(random_state=0).fit( xtrain, ytrain )

    metric = roc_auc_score( ytest, model.predict_proba(xtest)[:, 1])

    filename = 'model.pkl'
    joblib.dump(model, '/opt/airflow/models/' + filename)