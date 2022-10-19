from sqlite3 import connect
from mysqlutils import read_from_db, execute_query
from typing import Dict, List, Tuple

orders_result = """
    
    SELECT orders.order_id, customers.customer_name, customers.customer_phone
    , couriers.driver_name, couriers.driver_phone, products.prod_name,
    order_items.prod_qty, products.prod_price
    FROM orders
    INNER JOIN customers ON customers.customer_id = orders.order_id
    INNER JOIN couriers ON couriers.driver_id = orders.driver_id
    INNER JOIN order_items ON orders.order_id = order_items. order_id
    INNER JOIN products ON products.prod_id = order_items.prod_id

    """ 
    
price_summary = """

SELECT orders.order_id, customers.customer_name,
SUM(products.prod_price * order_items.prod_qty) AS total_price_per_id
FROM orders
INNER JOIN customers ON customers.customer_id = orders.order_id
INNER JOIN couriers ON couriers.driver_id = orders.driver_id
INNER JOIN order_items ON orders.order_id = order_items. order_id
INNER JOIN products ON products.prod_id = order_items.prod_id
GROUP BY orders.order_id 
ORDER BY customers.customer_name;

"""
    
    
def get_item_query(table_name):
    
    items_result = f"""
                SELECT * FROM {table_name}
                
                """
    
    return items_result

def insert_execute_records(courier_prod_dict, list_tuples, table_name, insert_or_ignore, connect):
    
    keys = tuple(courier_prod_dict) # unpacking dictionary keys into a tuple
    
    str1 =  f"""{insert_or_ignore} {table_name}("""
    str2 =  f"""VALUES("""
    
    index = 0
    for _ in keys:
        
        str1= str1 + f"""{keys[index]},"""
        str2 = str2 + f"""%s,"""
        index = index + 1
     
    str1 = str1[:-1] 
    str2 = str2[:-1]
    
    str3 = str1 + f""")"""
    str4 = str2 + f""")""" 
    
    insert_query = str3 + str4
        
    records_to_insert = list_tuples
    cursor = connect.cursor()
    cursor.executemany(insert_query, records_to_insert)
    connect.commit()
    
    
def insert_execute(courier_prod_dict, table_name, insert_or_ignore, connect):
    
    """
    
    In this function we make fstrings for a parametrised 
    insert query in mysql
    
    
    """
    keys = tuple(courier_prod_dict) # unpacking dictionary keys into a tuple
    values = tuple(courier_prod_dict.values())
    str1 =  f"""{insert_or_ignore} {table_name}("""
    str2 =  f"""VALUES("""
    
    index = 0
    for _ in keys:
        
        str1= str1 + f"""{keys[index]},"""
        str2 = str2 + f"""%s,"""
        index = index + 1
     
    str1 = str1[:-1] 
    str2 = str2[:-1]
    
    str3 = str1 + f""")"""
    str4 = str2 + f""")""" 
    
    insert_query = str3 + str4
    
    execute_query(insert_query, connect, values) 
    
    return insert_query

        
    
def delete_execute(table_name, id_name, id_number, connect):
    
    values = (id_number)
    delete_query = f"""
    
    DELETE FROM {table_name} WHERE {id_name} = %s
    
    
    """
    
    execute_query(delete_query, connect, values)
    
    return delete_query

def update_execute(table_name, courier_prod_dict, id, id_name, connect):
    
    """
    In this function we form fstrings for a parametrised update query.
    
    """
    keys = tuple(courier_prod_dict)
    values = tuple(courier_prod_dict.values()) 
    values_list = list(values)
    values_list.append(id)
    values_new = tuple(values_list)
    
    str1 = f"""UPDATE {table_name} SET"""
    
    index = 0
    for _ in keys:
        
        str1 = str1 + f""" {keys[index]} = %s,"""
        index = index + 1
        
    str1 = str1[:-1]
    str2 = f""" where {id_name} = %s"""
    
    update_query = str1 + str2
    
     
        
    execute_query(update_query, connect, values_new) 
    
    return update_query
    
  
def read_cafe_database(mysql_connection):
    
    """
    This function reads all tables from the cafe database. 
    These tables are stored into a tuple following the return.
    
    """
    
    prod_table = read_from_db(get_item_query('products'), mysql_connection)
    couriers_table = read_from_db(get_item_query('couriers'), mysql_connection)
    customers_table = read_from_db(get_item_query('customers'), mysql_connection)
    status_table = read_from_db(get_item_query('status'), mysql_connection)
    orders_table = read_from_db(get_item_query('orders'), mysql_connection)
    orders_items_table = read_from_db(get_item_query('order_items'), mysql_connection)
    
    return prod_table, couriers_table, customers_table, \
           status_table, orders_table, orders_items_table


def check_populate_database(*connection_db):
    
    """
    
    1) This functions receives a  tuple as an argument.
    2) This tuple comprises of all the tables in the cafe database.
    3) This tables are in form of a list of dictionaries.
    This function will go through each element in the list 
    of each table and check if that element exists or not in the 
    corresponding MySQL database. If it does not exist it will insert 
    it into the database.
    4) This is done using the INSERT IGNORE query of SQL
    5) It uses the functions designed above which are tailored 
    for Parametrized query.
    
    
    """
    
    #prod_list = cafe_database[0]
    
    my_sql_connection, cafe_database = connection_db
    table_names = ["products", "couriers", "customers", "status", 
                "orders", "order_items"]
    for list_item in cafe_database: #cafe_database is a tuple
        
        for index in range(len(list_item)): #list item is a list and may be products/couroer and so on
            
            keys = tuple(list_item[index]) # unpacking dictionary keys into a tuple
            values = tuple(list_item[index].values)
            required_query = insert_execute(keys, table_names[0], 'INSERT IGNORE') #get the insert query
            execute_query(required_query, my_sql_connection, values)
            

    
def process_order(orders_dict, connect):
    
     
     
    """
    This function receives an order dictionary based on the inputs from the user.
    This is not in the format of the designed database schema.
    Therefore, in order to bring it to the design of the database schema and insert 
    the records into the relevant tables, we have to have to split the user input
    based on the database schema and then call insert query
     
    In this case, we split the user input into 3 dictionaries which will access the 
    following tables:  
     
    """
     
    
    new_customer = {'customer_name': orders_dict['customer_name'], 
                    'customer_address': orders_dict['customer_address'], 
                    'customer_phone': orders_dict['customer_phone']}
     
     
    _ = insert_execute(new_customer, "customers", 'INSERT', connect)
    
    query_last = f"""
                SELECT LAST_INSERT_ID()
                
            """
    customer_id = read_from_db(query_last, connect)
    cust_id = customer_id[0]['LAST_INSERT_ID()']
    query = get_random_column("driver_id", "couriers")
    driver_id = read_from_db(query, connect)
    driver_id = driver_id[0]['driver_id']
    new_order = {'customer_id': cust_id, 'status_id': 2, 'driver_id': driver_id}
    _ = insert_execute(new_order, "orders", 'INSERT', connect)
    
    order_id = read_from_db(query_last, connect)
    order_id = order_id[0]['LAST_INSERT_ID()']
    
    #Now, we have to insert multiple records into the database
    #This is for the table order_items
    #We already have collected/processed as data as list of tuples 
    #from the user
    #It is just that we have to ammend the order id at the start of the tuple.
    #We cconvert the tuple to list as it is immutable and then convert it back to tuple 

    
    list_tuples = orders_dict['items']
    list_of_lists = [list(ele) for ele in list_tuples]
    for x in list_of_lists:
        x.insert(0, order_id)
    
    list_tuples2 = [tuple(x) for x in list_of_lists]

    my_dict = {'order_id':1, 'prod_id': 1, 'prod_qty': 1} #dummy dictionary
    _ = insert_execute_records(my_dict, list_tuples2, "order_items", 'INSERT', connect)
    
            
        
def get_random_column(column_name, table_name):
     
     
    query = f""" 
            SELECT {column_name} FROM {table_name}
            ORDER BY RAND()
            LIMIT 1  
            """
    return query
     
     
     
     
     
        
        
        
    
    
    


        
        
    
    


                
