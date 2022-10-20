def fstrings_paramtrised_query(courier_prod_dict, table_name, insert_or_ignore):
    
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
    return insert_query

def debug_update_execute(table_name, courier_prod_dict, id, id_name):
    
    
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
    
    str3 = str1 + str2
    return values_new
    

table_name = "couriers"
courier_prod_dict= {"driver_name": "John", "driver_phone": "07741719097"}
id = 3
id_name = "item_id"
values_new = debug_update_execute(table_name, courier_prod_dict, id, id_name)


def insert_execute_records(courier_prod_dict, list_tuples, table_name, insert_or_ignore, connect):
    
    """
    
    This function is used to insert multiple records into the database
    
    """
    
    keys = tuple(courier_prod_dict) # unpacking dictionary keys into a tuple
    
    

       
    