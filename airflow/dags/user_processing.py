import imp
from multiprocessing.spawn import import_main_path
from airflow import DAG
from datetime import datetime

with DAG('user_processing', start_date=datetime(2022,10,6),         schedule_interval='@daily', catchup=False)