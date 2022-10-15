import time
from typing import Dict, List, Tuple
from utils import delete_item, get_input_ints, dump_json, print_items,  \
    create_item, delete_item, validate_phone_number
from orders import create_prodids, update_order



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
    
    print("Updated Details: \n")   
    print_items(item_list)
    
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
    
    
    product_option = get_input_ints(while_range)
    return product_option


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
        
        
def get_item_menu_opts(item_option: int, options_tuple: Tuple, prod_list: List[Dict], courier_list: List[Dict], 
                        orders_dictlist: List[Dict], order_statuslist: List[str]):
    
       
    """
    This function has the product options. Notice the recursive call
    
    """
 
       
    if item_option == 0:
        
        user_option = get_main_menu()
        main_option = get_main_menu_opts(user_option)
        item_option = get_item_menu(main_option)
        get_item_menu_opts(item_option, options_tuple, prod_list, courier_list, orders_dictlist, order_statuslist)
        
    elif item_option == 1:
        
        print("Getting your " + options_tuple[0] + " list....Hold on!")
        time.sleep(4)
        print_items(options_tuple[-1])
        
    elif item_option == 2 and options_tuple[0] != "order":
        
        print_items(options_tuple[-1])
        inputted_list = create_item("Input: Name of the new " + options_tuple[0] + " please?\n", \
                        "Input: " + options_tuple[1].capitalize() + " of the new " + options_tuple[0] + " please?\n")
        name, price_phone = inputted_list
        my_dict = {"name": name, options_tuple[1]: price_phone}
        options_tuple[-1].append(my_dict)
        print("The appended list: ")
        print_items(options_tuple[-1])
        
    elif item_option == 3 and options_tuple[0] != "order":
        
        print_items(options_tuple[-1])
        inputted_list = create_item("Input: Name of the new " + options_tuple[0] + " please?\n", \
                        "Input: " + options_tuple[1].capitalize() + " of the new " + options_tuple[0] + " please?\n")
        name, price_phone = inputted_list
        my_dict = {"name": name, options_tuple[1]: price_phone}              
        update_product(options_tuple[-1], my_dict)
        print("The updated list: ")
        print_items(options_tuple[-1])
        
    elif item_option == 4 and options_tuple[0] != "order":
        _ = delete_item(options_tuple[-1])
    
    elif item_option == 2 and options_tuple[0] == "order":
        
        print_items(options_tuple[-1])
        inputted_list = create_item("Input: Please enter customer name\n", 
                                    "Input: Please enter customer address\n", 
                                    "Please enter customer phone number\n", 
                                    "Please enter courier index to select customer\n")
        customer_name, customer_address, customer_phone, courier_index = inputted_list
        order_status = 'Preparing'
        customer_phone = validate_phone_number(customer_phone)
        order_items = []
        prod_ids = create_prodids(prod_list, order_items)
        my_dict = {"customer_name": customer_name, "customer_address": customer_address, 
            "customer_phone": customer_phone, "courier": courier_index, 
            "status": order_status, "items": prod_ids}
        options_tuple[-1].append(my_dict)
        dump_json(options_tuple[-1], "data/orders.json")
        print("Appended order details:\n")
        print_items(options_tuple[-1])
        
    elif item_option == 3 and options_tuple[0] == "order":
        
        print_items(options_tuple[-1])
        range_limit = len(options_tuple[-1]) - 1
        print("You will now have to enter the order number for which you want the status modified\n")
        print_items(options_tuple[-1])
        user_order_index = get_input_ints(range_limit)
        range_limit = len(order_statuslist) - 1
        print_items(order_statuslist)
        print("You will now have to enter the status index to which you want the order to be updated to\n")
        user_status_index = get_input_ints(range_limit)
        options_tuple[-1][user_order_index]['status'] = order_statuslist[user_status_index]
        dump_json(options_tuple[-1], "data/orders.json")
        print("Appended order details:\n")
        print_items(options_tuple[-1])
        
    elif item_option == 4 and options_tuple[0] == "order":
        
        print_items(options_tuple[-1])
        range_limit = len(options_tuple[-1]) - 1
        print("You will now have to enter the index coresponding to the order you'd like updated\n")
        user_order_index = get_input_ints(range_limit)
        update_order(options_tuple[-1][user_order_index], prod_list)
      
    elif item_option == 5 and options_tuple[0] == "order":
        _ = delete_item(options_tuple[-1])
           
        
    else:
        product_option = print('Input index value within the range specified please:')
        product_option = get_input_ints(5)
        get_item_menu_opts (product_option, prod_list)
      
        
def get_status_types():
        
    status_types = ["Processing", "Accepted", "Preparing", "Ready", "Shipped", "Delivered"]
    return status_types