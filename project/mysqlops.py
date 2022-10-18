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
    
    
def get_item_query(table_name):
    
    items_result = f"""
                SELECT * FROM {table_name}
                
                """
    
    return items_result


def insert_execute(courier_prod_dict, table_name, insert_or_ignore, connect):
    
    """
    
    1) This function can be used for an INSERT or an
    INSERT IGNORE QUERY.
    2) Hence it receives a string (insert_or_ignore) which is
    either INSERT or INSERT IGNORE
    3) It receives the keys of the dictionary as a tuple
    which may be of length of 2 or 3.
    
    """
    
    keys = tuple(courier_prod_dict) # unpacking dictionary keys into a tuple
    values = tuple(courier_prod_dict.values())
    
    
    if len(keys) == 2:
        
        variable_1, variable_2 = keys
        
        insert_query = f"""
        
        {insert_or_ignore} {table_name}
        ({variable_1}, {variable_2}) VALUES (%s, %s)
        
        
        """
        
    elif len(keys == 3):
        
        variable_1, variable_2, variable_3 = keys
        
        insert_query = f"""
        
        INSERT INTO {table_name}
        ({variable_1}, {variable_2}, {variable_3}) VALUES (%s, %s, %s)
        
        """
        
    else:
        
        raise ValueError("Length of the tuple for the INSERT/INSERT IGNORE query \
                        is not in the supported range")
        
    execute_query(insert_query, connect, values) 
    
    return insert_query
        
    
def delete_execute(table_name, id_name, id_number):
    
    delete_query = f"""
    
    DELETE FROM {table_name} WHERE {id_name} = {id_number}
    
    
    """
    
    return delete_query

def update_execute(table_name, courier_prod_dict, id, item_id, connect):
    
     #sql_update_query = f"""UPDATE {table_name} set {variable_name} = %s where {id} = %s"""
     #return sql_update_query
     
    
        
    """
    
    1) This function can be used for an INSERT or an
    INSERT IGNORE QUERY.
    2) Hence it receives a string (insert_or_ignore) which is
    either INSERT or INSERT IGNORE
    3) It receives the keys of the dictionary as a tuple
    which may be of length of 2 or 3.
    
    """
    
    keys = tuple(courier_prod_dict)
    values = tuple(courier_prod_dict.values()) 
    values_list = list(values)
    values_list.append(id)
    values_new = tuple(values_list)
    
    
    if len(keys) == 1:
        
        variable_1, variable_2 = keys
        
        update_query = f"""
        
        UPDATE {table_name} SET {variable_1} = %s  where {item_id} = %s
        
        
        """
    
    elif len(keys) == 2:
        
        variable_1, variable_2 = keys
        
        update_query = f"""
        
        UPDATE {table_name} SET {variable_1} = %s, {variable_2} = %s where {item_id} = %s
        
        
        """
        
    elif len(keys == 3):
        
        variable_1, variable_2, variable_3 = keys
        
        update_query = f"""
        
        UPDATE {table_name} SET {variable_1} = %s, {variable_2} = %s , {variable_3} = %s where {item_id} = %s
        
        
        """
        
    else:
        
        raise ValueError("Length of the tuple for the INSERT/INSERT IGNORE query \
                        is not in the supported range")
        
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
    query = get_random_column("driver_id", "couriers")
    driver_id = read_from_db(query, connect)
    
    new_order = {'customer_id': customer_id, 'status_id': 2, 'driver_id': driver_id}
    _ = insert_execute(new_order, "orders", 'INSERT', connect)
    
    order_id = read_from_db(query_last, connect)
    
    #Now, we have to insert multiple records into the database
    
    item_qty = {'item_qty': orders_dict['item_qty']} #the dictionary must contin a tuple of item and quantity in a list #
    # that is we have to take the item and quantity from the end user and update in a list wit each entry
    
    _ = insert_execute(item_qty, "order_items", 'INSERT', connect )
    
            
        
def get_random_column(column_name, table_name):
     
     
    query = f""" 
            SELECT {column_name} FROM {table_name}
            ORDER BY RANDOM()
            LIMIT 1  
            """
     
     
     
     
     
        
        
        
    
    
    


        
        
    
    


                
