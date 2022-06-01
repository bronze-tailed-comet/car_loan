from airflow import DAG


from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.task_group import TaskGroup

from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime

from utils.create_connection import create_connection
from utils.extract_raw import extract_raw
from utils.save_data import save_data
from utils.train import train
from utils.predict import predict

with DAG('car_loan_ml_pipeline', schedule_interval=None, start_date=datetime(2022, 5, 30)) as dag:
 
    # task: 1
    create_conn = PythonOperator(
        task_id='create_connection',
        python_callable=create_connection
    )
    
    # task: 2
    create_car_loan_train_table = PostgresOperator(
        task_id="create_car_loan_train_table",
        postgres_conn_id='postgres_default',
        sql='sql/create_car_loan_train_table.sql'
    )

    # task: 3
    create_car_loan_pred_table = PostgresOperator(
        task_id="create_car_loan_pred_table",
        postgres_conn_id='postgres_default',
        sql='sql/create_car_loan_pred_table.sql'
    )
    
    # task: 4
    create_car_loan_serving_table = PostgresOperator(
        task_id="create_car_loan_serving_table",
        postgres_conn_id='postgres_default',
        sql='sql/create_car_loan_serving_table.sql'
    )
        
    # task: 5
    extract_raw = PythonOperator(
        task_id='extract_raw',
        python_callable=extract_raw
    )

    # task: 6
    ingest_raw = PythonOperator(
        task_id='save_raw_data',
        python_callable=save_data,
        op_args=['df_raw','car_loan_train']
    )
    
    # task: 7
    train = PythonOperator(
        task_id='train',
        python_callable=train
    )
    
    # task: 8
    predict = PythonOperator(
        task_id='predict',
        python_callable=predict
    )
    
    # task: 9
    ingest_pred = PythonOperator(
        task_id='save_pred_data',
        python_callable=save_data,
        op_args=['df_pred','car_loan_pred']
    )

    create_conn >> create_car_loan_train_table >> create_car_loan_pred_table >> create_car_loan_serving_table >> extract_raw >> ingest_raw >> train >> predict >> ingest_pred