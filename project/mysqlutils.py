import pymysql.cursors
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv
from typing import Dict, List, Tuple

from tomlkit import string

def create_connection():
    
    """
    
    This function will return a connection to mysql server. 
    The function reads a .env file which comprises of the host
    name, user name, password and the database name. 
    
    """
    
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
                                cursorclass=pymysql.cursors.DictCursor
                                
    )
                                
    return connection


def read_from_db(query: string, connect):
    
    """
    This function reads all tables of thefrom a MySQL database. It is important that a connection 
    should already have been established before this function is called 
    and hence the connect is passed as an argument.
    
    
    """
    #conn = create_connection()
    with connect.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def execute_query(query: string, connect, input_data: Tuple):
    
    """
    This function will execute a query on a MySQL database. 
    It is important that a connection to the MySQL database 
    should have been established before the query is executed. 
    
    When we say execute, it essentially means when we want to 
    add something to the database. 
    
    
    """

    with connect.cursor() as cursor:
        cursor.execute(query, input_data)
        connect.commit()
        


    
