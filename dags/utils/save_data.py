import pandas as pd
from sqlalchemy import create_engine

from utils.files_utils import load_file
import utils.ml_pipeline_config as config

db_engine = config.params["db_engine"]
db_schema = config.params["db_schema"]

def save_data(file_name, table_name):
    df = load_file(file_name)
    engine = create_engine(db_engine)
    df.to_sql(table_name, engine, schema=db_schema, if_exists='replace', index=False)