from typing import Dict, List, Tuple
from utils import get_input_ints, print_items

def update_order(order_dict: Dict, prod_list: List[Dict]):
    
    for key, value in order_dict.items():
        
        if key != "items":
            
            new_value = input("Input: Please enter the " + key + "? ")
            if new_value != "":
                order_dict[key] = new_value
        else:
            
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
    
    print("Menu of available drinks/food in the cafe \n")
    print_items(prod_list)
    range_items = len(prod_list) - 1
    print("You will now have to select the ids corresponding to the menu items you'd like to select\n")
    cont_option = 1
    while (cont_option == 1 ):
        prod_id = get_input_ints(range_items)
        if prod_id > range_items:
            print("Enter food/drink id in the range specified, please \n")
            prod_id = get_input_ints(range_items)
        item_list.append(prod_id)
        print("Do you wish to continue?\n")
        print("Enter 1 to continue or any other number to discontinue\n")
        cont_option = get_input_ints(10)
    
    return item_list


