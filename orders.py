from typing import Dict, List, Tuple
from utils import get_input_ints, print_items

def update_order(order_dict: Dict, prod_list: List[Dict]):
    
    for key, value in order_dict.items():
        
        if key != "items" and key != "order_id":
            
            new_value = input("Input: Please enter the " + key + "? ")
            if new_value != "":
                order_dict[key] = new_value
                
        if key == "items":
            
            new_value = input("Input: Do you want to append menu your items? Leave this blank if  you do not wish to edit your menu \n")
            if new_value != "":
                order_dict[key] = create_prodids(prod_list, order_dict[key])   
                    
    return order_dict

def create_prodids(prod_list, item_list):
    
    """
    This function will create a list of product ids to be updated into the order dictionary for a
    specific order. It receives the product list which will help the end user to update his/her 
    order.
    
    """
    
    range_items = len(prod_list) 
    print("You will now have to select the ids and quantities \ncorresponding to the menu items you'd like to select")
    cont_option = 1
    while (cont_option == 1 ):
        print("Product id:")
        prod_id = get_input_ints(range_items)
        print("Item quantity:")
        qty_item = get_input_ints(5)
        item_list.append((prod_id, qty_item))
        print("Do you wish to continue?\n")
        print("Enter 1 to continue or any other number to discontinue\n")
        cont_option = get_input_ints(10)
    
    return item_list


