from mysqlutils import read_from_db, execute_query

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


def insert_query(*keys, table_name, insert_or_ignore):
    
    """
    
    1) This function can be used for an INSERT or an
    INSERT IGNORE QUERY.
    2) Hence it receives a string (insert_or_ignore) which is
    either INSERT or INSERT IGNORE
    3) It receives the keys of the dictionary as a tuple
    which may be of length of 2 or 3.
    
    """
    
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
        
    
    return insert_query
        
    
def delete_item(table_name, id_name, id_number):
    
    delete_query = f"""
    
    DELETE FROM {table_name} WHERE {id_name} = {id_number}
    
    
    """
    
    return delete_query

def update_query(table_name, variable_name, id):
    
     sql_update_query = f"""UPDATE {table_name} set {variable_name} = %s where {id} = %s"""
     return sql_update_query
    
  
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
            insert_query = insert_query(keys, table_names[0], 'INSERT IGNORE') #get the insert query
            execute_query(insert_query, my_sql_connection)
            
            
        
        
        
        
    
    
    


        
        
    
    


                
