params = {
    "db_engine": "postgresql+psycopg2://airflow:airflow@postgres/airflow",
    "db_schema": "public",
    "db_experiments_table": "experiments",
    "db_batch_table": "car_loan_train",
    "test_split_ratio": 0.2,
    "features": ['main_account_loan_no',
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
                 'sub_account_disbursed_loan'],
    "target": ['loan_default']
    
}   