import pandas as pd
import numpy as np
import joblib
from sqlalchemy import create_engine
import json

import dags.utils.ml_pipeline_config as config

db_engine = config.params["db_engine"]
db_schema = config.params["db_schema"]

def make_features_col(x, features):
    
    return json.dumps(dict(x[features]))


def load_to_sql(X, features):
    
    X['features'] = X.apply( lambda x: make_features_col(x, features), axis=1 )

    X = X[['customer_id','features','pred','pred_proba']].copy()
    
    engine = create_engine(db_engine)
    
    X.to_sql('car_loan_serving', engine, schema=db_schema, if_exists='append', index=False)
    

def predict(X):
    
    features = [ 'main_account_loan_no',
                 'main_account_active_loan_no',
                 'main_account_overdue_no',
                 'main_account_outstanding_loan',
                 'main_account_sanction_loan',
                 'main_account_disbursed_loan',
                 'sub_account_loan_no',
                 'sub_account_active_loan_no',
                 'sub_account_overdue_no',
                 'sub_account_outstanding_loan',
                 'sub_account_sanction_loan',
                 'sub_account_disbursed_loan' ]

    X = pd.DataFrame( X, index=[0] )
    
    model = joblib.load('models/model.pkl')
    X['pred'] = model.predict( X[features] )
    X['pred_proba'] = model.predict_proba( X[features] )[:, 1]
    
    load_to_sql(X, features)

    return np.round(X['pred_proba'].iloc[0],3)