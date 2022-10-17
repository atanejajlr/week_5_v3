import time
from typing import Dict, List, Tuple
from utils import delete_item, get_input_ints, dump_json, print_items,  \
    create_item, delete_item, validate_phone_number, print_items_formatted
from orders import create_prodids, update_order
from mysqlutils import read_from_db, get_item_query



def update_product(item_list, my_dict):
    
    '''
    This is the function for updating the product
    
    '''
      
    product_index = len(item_list) + 100
    product_index = int(input('Input:Index Value that you want updated?'))
    
    while product_index > len(item_list):
        
        product_index = int(input('Input: Correct index value, please ?'))
        
    #new_prod = input(input_string)
    item_list[product_index] = my_dict
    return product_index
    
    #print("Updated Details: \n")   
    #print_items(item_list)
    
def get_main_menu(): 
    
    """ 
    This function displays the menu options from the end user. This could be either 0 or 1
    0 is for exiting out of the application and
    1 is for getting the list of products
    2 is for getting the list of couriers
    3 if for getting the list of orders
    
    """
    
    print("Welcome to the cafe")
    print("Select from the following menu options:")
    print("Select 0  to exit out of the application\n OR")
    print ("Select 1 to see the list of products\n OR")
    print("Select 2 to see the list of couriers\n OR")
    print("Select 3 to see the list of orders")
    user_option = get_input_ints(3)
    return user_option

def get_item_menu(user_selection: str):
    
    """
    This function displays the product options
    
    """
    
    print("You are now in the " + user_selection + " menu\n")
    print("Please read the below possible options\n\n")
    print("Select 0 to return to the main menu \n OR")
    print("Select 1 to print the " + user_selection + "s list \n OR")
    print("Select 2 to create new " + user_selection + " \n OR")
    
    if user_selection != "order":
        
        print("Select 3 to update an existing " + user_selection + " \n OR")
        print("Select 4 to delete an existing " + user_selection + " \n OR")
        while_range = 4
    
    else:
        
        print("Select 3 to update an existing " + user_selection + " status" + " \n OR")
        print("Select 4 to update an existing " + user_selection + " content" + " \n OR")
        print("Select 5 to delete an existing " + user_selection + " \n OR")
        while_range = 5
    
    
    crud_option = get_input_ints(while_range)
    return crud_option


def get_main_menu_opts(main_option: int, prod_list: List[Dict], couriers_list: List[Dict], 
                    orders_dictlist: List[Dict], dump_json_sql, *sql_nosql_inputs):
    
  
    """
    This has the main menu options. Note the recursive call.
    
    """
    
    if main_option == 0:
            
        print("The application will now exit. Exiting application...")
        #dump_json_sql(prod_list, "data/products.json")
        dump_json_sql(*sql_nosql_inputs)
        dump_json_sql(*sql_nosql_inputs)
        dump_json_sql(*sql_nosql_inputs)
        time.sleep(2)
        exit()
            
    elif main_option == 1:
        
        return "product", "price", prod_list
    
    elif main_option == 2:
        
        return "courier", "phone number", couriers_list
    
    elif main_option == 3:
        
        return "order", orders_dictlist
                
    else:
            
        main_option = print('Input either 0 or 1 or 2 or 3 as advised above:')
        main_option = get_input_ints(3)
        get_main_menu_opts(main_option, prod_list, couriers_list, orders_dictlist)
        
        
def get_item_menu_opts(crud_option: int, item_opts_possible: Tuple, connect, main_menu_selection, sql_no_sql_create):
    
       
    """
    This function has the CRUD operations. That is, either: 
    
    1) We read from the database and print outputs (Read)
    2) We create soemthing new in the database (create either a product or courier or an order)
    3) We update the database (either a product, courier or order)
    4) We delete an objbect from the database (product, courier or an order)
    
    Notice the recursive call
    
    """
 
       
    if crud_option == 0:
        
        user_option = get_main_menu()
        main_option = get_main_menu_opts(user_option)
        crud_option = get_item_menu(main_option)
        #get_item_menu_opts(crud_option, item_opts_possible, prod_list, courier_list, orders_dictlist, order_statuslist)
        get_item_menu_opts(crud_option, item_opts_possible, connect, main_menu_selection)
        
    elif crud_option == 1: # reading from the database (sql or no sql)
        
        print("Getting your " + item_opts_possible[0] + " list....Hold on!")
        time.sleep(4)
        print_items_formatted(item_opts_possible[-1])
          
    elif crud_option == 2 and item_opts_possible[0] == "product": # creating a new product in the database
        
        create_product_courier(item_opts_possible, "prod_name", "prod_price", "products", connect, sql_no_sql_create)
        
    elif crud_option == 2 and item_opts_possible[0] == "courier": # creating a new courier in the database
        
        create_product_courier(item_opts_possible, "driver_name", "driver_phone", "couriers", connect, sql_no_sql_create)
        
    elif crud_option == 3 and item_opts_possible[0] == "product": # updating the product database
        
        # print_items(item_opts_possible[-1])
        # inputted_list = create_item("Input: Name of the new " + item_opts_possible[0] + " please?\n", \
        #                 "Input: " + item_opts_possible[1].capitalize() + " of the new " + item_opts_possible[0] + " please?\n")
        # name, price_phone = inputted_list
        # my_dict = {"name": name, item_opts_possible[1]: price_phone}
        my_dict = create_product_courier(item_opts_possible, "prod_name", "prod_price", "products", connect, sql_no_sql_create)             
        product_index = update_product(item_opts_possible[-1], my_dict)
        #sql_no_sql_update(connect, my_dict, main_menu_selection)
        print("The updated list: ")
        print_items_formatted(item_opts_possible[-1])
        
    elif crud_option == 3 and item_opts_possible[0] == "courier": # updating the courier database
        my_dict = create_product_courier(item_opts_possible, "driver_name", "driver_phone", "couriers", connect, sql_no_sql_create)
        product_index = update_product(item_opts_possible[-1], my_dict)
        
        
    elif crud_option == 4  or crud_option == 5: # deleting from the database
        _ = delete_item(item_opts_possible[-1])
    
    elif crud_option == 2 and item_opts_possible[0] == "orders": # creating 
        
        print_items(item_opts_possible[-1])
        inputted_list = create_item("Input: Please enter customer name\n", 
                                    "Input: Please enter customer address\n", 
                                    "Please enter customer phone number\n", 
                                    "Please enter courier index to select customer\n")
        customer_name, customer_address, customer_phone, courier_index = inputted_list
        order_status = 'Preparing'
        customer_phone = validate_phone_number(customer_phone)
        order_items = []
        #prod_ids = create_prodids(prod_list, order_items)
        # my_dict = {"customer_name": customer_name, "customer_address": customer_address, 
        #     "customer_phone": customer_phone, "courier": courier_index, 
        #     "status": order_status, "items": prod_ids}
        item_opts_possible[-1].append(my_dict)
        dump_json(item_opts_possible[-1], "data/orders.json")
        print("Appended order details:\n")
        print_items(item_opts_possible[-1])
        
    elif crud_option == 3 and item_opts_possible[0] == "order": #updating order in the database
        
        print_items(item_opts_possible[-1])
        range_limit = len(item_opts_possible[-1]) - 1
        print("You will now have to enter the order number for which you want the status modified\n")
        print_items(item_opts_possible[-1])
        user_order_index = get_input_ints(range_limit)
        #range_limit = len(order_statuslist) - 1
        #print_items(order_statuslist)
        print("You will now have to enter the status index to which you want the order to be updated to\n")
        user_status_index = get_input_ints(range_limit)
        #item_opts_possible[-1][user_order_index]['status'] = order_statuslist[user_status_index]
        dump_json(item_opts_possible[-1], "data/orders.json")
        print("Appended order details:\n")
        print_items(item_opts_possible[-1])
        
    elif crud_option == 4 and item_opts_possible[0] == "order": #updating order in the database
        
        print_items(item_opts_possible[-1])
        range_limit = len(item_opts_possible[-1]) - 1
        print("You will now have to enter the index coresponding to the order you'd like updated\n")
        user_order_index = get_input_ints(range_limit)
        #update_order(item_opts_possible[-1][user_order_index], prod_list)
      
         
    else:
        product_option = print('Input index value within the range specified please:')
        product_option = get_input_ints(5)
        #get_item_menu_opts (product_option, prod_list)
      
        
def get_status_types():
        
    status_types = ["Processing", "Accepted", "Preparing", "Ready", "Shipped", "Delivered"]
    return status_types


def create_product_courier(item_opts_possible, key_1, key_2, table_name, connect, sql_no_sql_create):
    
    print_items_formatted (item_opts_possible[-1])
    inputted_list = create_item("Input: Name of the new " + item_opts_possible[0] + " please?\n", \
            "Input: " + item_opts_possible[1].capitalize() + " of the new " + item_opts_possible[0] + " please?\n")
    prod_name, prod_price = inputted_list
    my_dict = {key_1: prod_name, key_2: prod_price}
    sql_no_sql_create(my_dict, table_name, "INSERT", connect) #creating a prod or courier row in the sql /cafe database now
    prod_courier_table = read_from_db(get_item_query(table_name), connect)
    print("The appended list: ")
    print_items_formatted (prod_courier_table)
    return my_dict