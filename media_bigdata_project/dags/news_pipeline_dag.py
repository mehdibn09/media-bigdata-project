from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

PROJECT_DIR = '/opt/airflow/project'

with DAG(
    dag_id='news_bigdata_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule_interval='@hourly',
    catchup=False,
    tags=['bigdata', 'news', 'medallion'],
) as dag:
    scrape = BashOperator(
        task_id='scrape_articles',
        bash_command=f'cd {PROJECT_DIR} && python scrapers/scraper_hespress.py'
    )
    bronze_to_silver = BashOperator(
        task_id='bronze_to_silver',
        bash_command=f'cd {PROJECT_DIR} && python pipelines/bronze_to_silver.py'
    )
    silver_to_gold = BashOperator(
        task_id='silver_to_gold',
        bash_command=f'cd {PROJECT_DIR} && python pipelines/silver_to_gold.py'
    )
    quality = BashOperator(
        task_id='data_quality_checks',
        bash_command=f'cd {PROJECT_DIR} && python quality/data_quality_checks.py'
    )
    load_dw = BashOperator(
        task_id='load_to_postgres',
        bash_command=f'cd {PROJECT_DIR} && python pipelines/load_to_postgres.py'
    )

    scrape >> bronze_to_silver >> quality >> silver_to_gold >> load_dw
