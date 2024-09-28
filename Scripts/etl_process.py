import pandas as pd
from sqlalchemy import create_engine

# connection string for mysql database
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

# Extract
# extract source data from both the file
df_emp = pd.read_csv('data/employees.csv')
df_emp.to_sql("staging_employees",mysql_engine,if_exists='replace',index=False)
df_sal = pd.read_json('data/salary.json')
df_sal.to_sql("staging_salary",mysql_engine,if_exists='replace',index=False)

# Transform
# a) convert ename to upper case
# b) replace the null values from commission with 0
# c) total_salary = sal + comm

query ="""select  e.eno,upper(e.ename) as upper_name,e.hiredate,s.salary,ifnull(s.commission,0) as commission, 
s.salary+s.commission as total_salary from staging_employees as e 
join staging_salary as s on e.eno = s.eno"""
df = pd.read_sql(query,mysql_engine)

# Load
df.to_sql("employees_details",mysql_engine,if_exists='replace',index=False)