import pyodbc
import pandas as pd

# cnxn = pyodbc.connect(driver = '{MySQL ODBC 5.3 ANSI Driver}', host='localhost:3306', database='demo_db', 
#                       Trusted_Connection = 'yes')

# connection_string = (
#     'DRIVER=MySQL ODBC 5.3 ANSI Driver;'
#     'SERVER=localhost:3306;'
#     'DATABASE=demo_db;'
#     'UID=ataneja;'
#     'PWD=myownphd;'
#     'charset=utf8mb4;'
    
    
#)

#cnxn = pyodbc.connect(connection_string)

import pymysql.cursors
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
# Connect to the database
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * from person"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

