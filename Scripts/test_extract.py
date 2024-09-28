import pandas as pd
import pytest
from sqlalchemy import create_engine
# connection string for mysql database
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

def test_dataExtrcatFromEmployeesFile():
    df_expected = pd.read_csv('data/employees.csv')
    query ="""select * from staging_employees"""
    df_actual = pd.read_sql(query,mysql_engine)
    assert df_actual.equals(df_expected),"Data extrcation from employees.csv is failed"

def test_dataExtrcatFromSalaryFile():
    df_expected = pd.read_json('data/salary.json')
    query ="""select * from staging_salary"""
    df_actual = pd.read_sql(query,mysql_engine)
    assert df_actual.equals(df_expected),"Data extrcation from salary.json is failed"


