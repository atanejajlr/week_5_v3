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
    
    
    




# def insert_prod(keys, values):
    
    
#     prod_name, prod_price = keys
#     value_name, value_price = values
    
#     insert_query = f"""
    
#     INSERT IGNORE INTO products 
#     ({prod_name}, {prod_price}) 
#     VALUES 
#     ('{value_name}', {value_price});
    
#     """
    
#     return insert_query

# def insert_courier(keys, values):
    
    
#     driver_name, driver_phone = keys
#     value_name, value_phone = values
    
#     insert_query = f"""
    
#     INSERT IGNORE INTO couriers
#     ({driver_name}, {driver_phone}) 
#     VALUES 
#     ('{value_name}', '{value_phone}');
    
#     """
    
#     return insert_query


# def insert_customers(keys, values):
    
    
#     customer_name, customer_address, customer_phone = keys
#     value_name, value_address, value_phone = values
    
#     insert_query = f"""
    
#     INSERT IGNORE INTO couriers
#     ({customer_name}, {customer_address}, {customer_phone}) 
#     VALUES 
#     ('{value_name}', '{value_address}', '{value_phone}');
    
#     """
    
#     return insert_query

# def insert_order_items(table_name, keys, values):
    
#     order_id, cust_prod_id, id_qty = keys
#     value_1, value_2, value_3 = values
    
#     insert_query = f"""
    
#     INSERT IGNORE INTO {table_name}
#     ({order_id}, {cust_prod_id}, {id_qty}) 
#     VALUES 
#     ({value_1}, {value_2}, {value_3});
    
#     """
    
#     return insert_query


def insert_query(*keys, table_name):
    
    if len(keys) == 2:
        
        variable_1, variable_2 = keys
        
        insert_query = f"""
        
        INSERT INTO {table_name}
        ({variable_1}, {variable_2}) VALUES (%s, %s)
        
        
        """
        
    else:
        
        variable_1, variable_2, variable_3 = keys
        
        insert_query = f"""
        
        INSERT INTO {table_name}
        ({variable_1}, {variable_2}, {variable_3}) VALUES (%s, %s, %s)
        """
    
    return insert_query
        
    
def delete_item(table_name, id_name, id_number):
    
    delete_query = f"""
    
    DELETE FROM {table_name} WHERE {id_name} = {id_number}
    
    
    """
    
    return delete_query

def update_query(table_name, variable_name, id):
    
     sql_update_query = f"""UPDATE {table_name} set {variable_name} = %s where {id} = %s"""
     return sql_update_query
 
 
#19/10/2022
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
        
    elif len(keys) == 3:
        
        variable_1, variable_2, variable_3 = keys
        
        insert_query = f"""
        
        {insert_or_ignore} {table_name}
        ({variable_1}, {variable_2}, {variable_3}) VALUES (%s, %s, %s)
        
        """
        
    else:
        
        raise ValueError("Length of the tuple for the INSERT/INSERT IGNORE query \
                        is not in the supported range")
        
    execute_query(insert_query, connect, values) 
    
    return insert_query


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
        
        variable_1 = keys
        
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
    
    


        
        
    
    


                
