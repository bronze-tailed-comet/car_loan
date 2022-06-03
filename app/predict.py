import pandas as pd
import numpy as np
import joblib
from sqlalchemy import create_engine
import json
from os.path import exists

import dags.utils.ml_pipeline_config as config

db_engine = config.params["db_engine"]
db_schema = config.params["db_schema"]

def make_features_col(x, features):
    
    return json.dumps(dict(x[features]))


def load_to_sql(X, features):
    
    X['features'] = X.apply( lambda x: make_features_col(x, features), axis=1 )

    X = X[['customer_id','features','pred','pred_proba']].copy()
    
    engine = create_engine(db_engine)
    
    try:
        X.to_sql('car_loan_serving', engine, schema=db_schema, if_exists='append', index=False)
        resp = 1
        print("SQL OK")
    except Exception as e:
        print("error SQL",e)
        resp = e
        
    return resp
    

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
    
    model_path = 'models/model.pkl'
    
    if exists(model_path):
        
        model = joblib.load('models/model.pkl')
        X['pred'] = model.predict( X[features] )
        X['pred_proba'] = model.predict_proba( X[features] )[:, 1]
        
        print("model found")
        
    else:
        
        return {
                'status':'500',
                'response': {'message':'Model does not exist'}
        }
    
        
    resp_sql = load_to_sql(X, features)
        
    if(resp_sql == 1):
            
        return {
            'status':'200',
            'response': {'pred':np.round(X['pred_proba'].iloc[0],3),'message':'success'}
        }
        
    else:
            
        return {
            'status':'503',
            'response': {'pred':np.round(X['pred_proba'].iloc[0],3), 'message':'Something went wrong with the database'}
        }