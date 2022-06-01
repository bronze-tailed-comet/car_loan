import pandas as pd
import joblib
import json

from utils.files_utils import save_file, load_file

import utils.ml_pipeline_config as config


def make_features_col(x, features):
    
    return json.dumps(dict(x[features]))


def predict():
    
    model = joblib.load('/opt/airflow/models/model.pkl')
    
    df = load_file('df_raw')

    features = config.params['features']

    df['pred'] = model.predict( df[features] )
    df['pred_proba'] = model.predict_proba( df[features] )[:, 1]

    df['features'] = df.apply( lambda x: make_features_col(x, features), axis=1 )
    
    save_file(df[['customer_id','features','pred','pred_proba']], 'df_pred')