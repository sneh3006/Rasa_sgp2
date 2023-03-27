import cx_Oracle as cx
import sqlalchemy
import pandas as pd

# Use your database credentials below
DATABASE = "DB"
SCHEMA   = "DEV"
PASSWORD = "password"

# Generating connection string
connstr  = "oracle://{}:{}@{}".format(SCHEMA, PASSWORD, DATABASE)
conn     = sqlalchemy.create_engine(connstr)

# Fetching the data from the selected table using SQL query
RawData= pd.read_sql_query("select * from [EMP].[Employee_table] where countryCode='US'", conn)
RawData.head()