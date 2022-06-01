from airflow import settings
from airflow.models import Connection

def create_connection():
    conn = Connection(
            conn_id="postgres_default",
            conn_type="Postgres",
            host="postgres",
            login="airflow",
            password="airflow",
            schema="airflow"
    ) #create a connection object
    session = settings.Session() # get the session
    session.add(conn)
    session.commit()