import os
import pytest
from unittest.mock import patch
from utils import get_input_ints, read_dictlist, delete_item, create_item
from operations import get_main_menu, get_main_menu_opts, get_item_menu, \
create_prodids, create_product_courier
from orders import update_order
from mysqlutils import read_from_db
from mysqlops import get_item_query, insert_execute, \
insert_execute_records, delete_execute, update_execute
import pymysql.cursors
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv


def unit_tests_fixture_close():
    
    connection = connect_mysql()
    drop_query = f"""DROP TABLE IF EXISTS customers;"""
    execute_queries(connection, drop_query)
    drop_query = f"""DROP TABLE IF EXISTS products;"""
    execute_queries(connection, drop_query)
    
@pytest.fixture(scope="module", autouse=True)
def  unit_tests_fixture_start():
    connection = connect_mysql()
    drop_query = f"""DROP TABLE IF EXISTS customers;"""
    execute_queries(connection, drop_query)
    drop_query = f"""DROP TABLE IF EXISTS products;"""
    execute_queries(connection, drop_query)
    query_create_customers = """ CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(50),
    customer_address VARCHAR(1000),
    customer_phone VARCHAR(50)
    );"""
  
    execute_queries(connection, query_create_customers)
    query_create_products = """CREATE TABLE products (
  
    prod_id INT AUTO_INCREMENT PRIMARY KEY,
    prod_name VARCHAR(50),
    prod_price DECIMAL (5,2)
    );"""
    
    execute_queries(connection, query_create_products)
    yield
    unit_tests_fixture_close()

def execute_queries(connect,query):
    with connect.cursor() as cursor:
        cursor.execute(query)
        connect.commit()
   
def connect_mysql():
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    return connect


@patch("builtins.input")
def test_get_input_ints(mock_input):
    
    #assemble
    range_limit = 3
    mock_input.return_value = 2
    expected_result = 2
    
    #act
    actual_result = get_input_ints(range_limit)
    
    #assert 
    assert actual_result == expected_result
 
  
@patch("builtins.input", side_effect=["5z", "1"])  
def test_get_input_ints_exception(mock_input):
    
    #assemble
    range_limit = 3
    expected_result = 1
    
    
    #act
    actual_result = get_input_ints(range_limit)
        
    
    #assert 
    assert actual_result == expected_result
    

@patch("builtins.input", side_effect=["5z", "7", "2"])  
def test_get_input_ints_range(mock_input):
    
    #assemble
    range_limit = 3
    expected_result = 2
    
    
    #act
    actual_result = get_input_ints(range_limit)
        
    
    #assert 
    assert actual_result == expected_result
 
 
@patch("builtins.input")   
def test_get_main_menu(mock_input):
    
    #assemble
    mock_input.return_value = 2
    expected_result = 2
    
    #act
    actual_result = get_main_menu()
    
    #assert
    assert actual_result == expected_result
    
@patch("builtins.input", side_effect=["11z", 5, 2])   
def test_get_main_menu_range(mock_input):
    
    #assemble
    expected_result = 2
    
    #act
    actual_result = get_main_menu()
    
    #assert
    assert actual_result == expected_result
    
   
def test_read_dictlist():
    
    #assemble
  
    file_name = "tests/test_data/orders.json"
    expected_result = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", 
                        "customer_phone": "0789887334", "courier": 2, "status": "Preparing", "items": [1, 2]}, 
                        {"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                        "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}]
    
    #act
    actual_result = read_dictlist(file_name)
    
    #assert 
    assert actual_result == expected_result
 

  
@patch("builtins.input")  
def test_get_item_menu(mock_input):
    
    #assemble
    user_selection = "order"
    mock_input.return_value = 4
    expected_result = 4
    
    #act
    actual_result = get_item_menu(user_selection)
    
    #assert
    assert actual_result == expected_result
    
# def test_get_main_menu_opts():
    
#     #assemble
#     user_option = 2
#     prod_list = [{"name": "Coke Zero", "price": 2.0}, {"name": "Sprite", "price": 1.8}]    
#     courier_list = [{"name": "John", "phone number": "0789887334"}, {"name": "Tim", "phone number": "0789887156"}]
#     orders_dictlist = [{"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
#                     "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}]
    
#     expected_result = ("courier", "phone number", courier_list)
#     #act
#     actual_result = get_main_menu_opts(user_option, prod_list, courier_list, orders_dictlist)
    
#     #assert
#     assert actual_result == expected_result
    
@patch('builtins.input', side_effect=["Diet Lemonade", "2.80"])  
def test_create_item(mock_input):
    
  
  #assemble
  
  options_tuple = ("product", "price")
  expected_result = ["Diet Lemonade", "2.80"]
  
  #act
  
  actual_result = create_item("Input: Name of the new " + options_tuple[0] + " please?\n", \
                        "Input: " + options_tuple[1].capitalize() + " of the new " + options_tuple[0] + " please?\n")  
   
    
  #assert
  
  assert actual_result == expected_result 
  
def test_get_item_query():
    
    #assemble
    
    table_name = "orders"
    expected_result = f"""
    
    SELECT * FROM {table_name}
    
    """
    
    #act
    actual_result = get_item_query(table_name)
    
    #assert
    
    actual_result == expected_result
    
def test_insert_execute_records():
    
    
    
#courier_prod_dict, list_tuples, table_name, insert_or_ignore, connect):

#assemble

    courier_prod_dict = {"customer_name": "XYZ", "customer_phone": "07741719089"}
    list_tuples = [("Jim", "07741718234"), ("Jenny", "07741718235")]
    insert_or_ignore = 'INSERT'
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    #expected_result
    
    expected_result = """INSERT customers(customer_name,customer_phone)VALUES(%s,%s)"""
    #act
    
    actual_result = insert_execute_records(courier_prod_dict, list_tuples, "customers", 
                                        insert_or_ignore, connect)
    
    #act
    
    assert expected_result == actual_result
    
def test_insert_execute():
    
    #assemble
    
    courier_prod_dict = {"customer_name": "unittest2", "customer_phone": "07741719031"}
    table_name = "customers"
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    insert_or_ignore = 'INSERT'
    expected_result = """INSERT customers(customer_name,customer_phone)VALUES(%s,%s)"""
    #act
    
    actual_result = insert_execute(courier_prod_dict, table_name, insert_or_ignore, connect)
    
    #assert
    
    assert actual_result == expected_result
    
def test_delete_execute():
    
    #assemble
    table_name = "customers"
    id_name = "customer_id"
    id_number = 2
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    expected_result = """
    DELETE FROM customers WHERE customer_id = %s"""
    #act
    actual_result = delete_execute(table_name, id_name, id_number, connect)
    
    #assert
    assert actual_result == expected_result
    
def test_update_execute():
    
    #assemble
    table_name = 'customers'
    courier_prod_dict = {"customer_name": "XYZ2", "customer_phone": "07732319089"}
    id = 2
    id_name = "customer_id"
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    expected_result = """UPDATE customers SET customer_name = %s, customer_phone = %s where customer_id = %s"""
    #act
    actual_result = update_execute(table_name, courier_prod_dict, id, id_name, connect)
    
    #assert
    assert actual_result == expected_result
    
def test_read_from_db():
    
    #assemble
    
    table_name = "products"
    query = f"""SELECT * FROM {table_name}"""
    
    #act
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    expected_result = [{'prod_id': 1, 'prod_name': 'Coke Zero'}]
    #act
    actual_result = read_from_db(query, connect)
    
   #assert
    actual_result == expected_result

@patch('builtins.input', side_effect=["Diet Lemonade", 2.80])      
def test_create_product_courier(mock_input):
    
    #assemble
    
    key_1 = "prod_name"
    key_2 = "prod_price"
    table_name = "products"
    sql_no_sql_create = insert_execute
    
    load_dotenv("tests/test_data/.env1")
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connect = pymysql.connect(host=host,
                                user=user,
                                password=password,
           
           
                                database=database,
                                cursorclass=pymysql.cursors.DictCursor)
    
    prod_list =  [{'prod_name': "Coke Zero", 'prod_price': 2.75}]
    item_opts_possible = ("product", "price", prod_list)
    expected_result = [{'prod_name': "Coke Zero", 'prod_price': 2.75}, 
                    {'prod_name': "Diet Lemonade", 'prod_price': 2.80}]
    
    #act
    
    actual_result = create_product_courier(item_opts_possible, key_1, key_2, table_name, 
                                            connect, sql_no_sql_create)
    
    #assert
    actual_result == expected_result
    
    
    
    
    
    

    



  
  

    

    
    
    
    
   
    
    