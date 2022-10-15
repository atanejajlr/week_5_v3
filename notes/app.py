import pymysql.cursors
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv

def create_connection():
    
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    print(host)
    print(user)

    # Connect to the database
    connection = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor
                                
    )
                                
    
    return connection

conn = create_connection()

with conn.cursor() as cursor: 
    
    cursor.execute("""
                SELECT * FROM products
                """)

    result = cursor.fetchall()

print("result = ", result)



for row in result:
    print("product name:", (row['name']))

for row in result:
    print("product price:", float(row['price']))
    
def read_from_db(query):
    conn = create_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def execute_query(query):
    conn = create_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    
    
    
    
    

