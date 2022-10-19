import json
from typing import Dict, List, Tuple
import phonenumbers
import tabulate

def get_input_ints(range_limit: int):
    
    """
    
    This function receives the "integer" values from the end user and thros an error if the value
    is not an integer forcing the user to re-enter
    
    """
    
    user_option = 1e3
    
    while user_option > range_limit:
        try:
            user_option = int(input('Your input please . Please input value in the range specified:')) 
        except ValueError:
            print("You must enter an integer")
    
    return user_option


def delete_item(item_list: List):
    
    """
    
    This function deletes an item from a list as defined by the user
    
    """
    
    print_items(item_list)
    product_index = int(input('Input: Index Value to be deleted?'))
    while product_index > len(item_list):
        product_index = int(input('Input: Correct index value to be deleted, please?'))
    del item_list[product_index]
    print("Revised List:")   
    print_items(item_list)
    return item_list
    
 
def read_dictlist(file_name):
    
    """
    This function reads a list of dictionaries from a file
    The json module is used because all the files are now  
    in the json format. The content is a list of dictionaries.
    
    """
    
    try:
        
        with open(file_name, 'r') as read_file:
            data = json.load(read_file)
            return data
    except Exception as error:
        print("Error reading the orders details!", error)
        
def validate_phone_number(phone_number):
    
    parsed_num =  phonenumbers.parse(phone_number, "GB")
    valid_number = phonenumbers.is_valid_number(parsed_num)
    
    
    while valid_number is False:
        
        print("The phone number enetered does not seem correct\n")
        phone_number = input("Input: Enter phone number without the country code without any spaces\n")
        parsed_num=  phonenumbers.parse(phone_number, "GB")
        valid_number = phonenumbers.is_valid_number(parsed_num)
    
    return phone_number

def print_items(item_list: List[Dict]):
    
    """
    
    This function prints the products
    
    """
    
    print("The current details are as follows:\n")
    
    for index, value in enumerate(item_list):
        print(index, value)
 
def print_items_formatted(list_dict):
    
    """
    This function prints the dictionaries formatted in tabular form 
    using the Python library tabulate
    
    """
    header = list_dict[0].keys()
    rows =  [dict_item.values() for dict_item in list_dict]
    print(tabulate.tabulate(rows, header))
    

def print_dict_formatted(headers, my_dict):
    
    print(tabulate.tabulate(my_dict.items(), headers = headers))  
    
    
def dump_json(*sql_nosql_inputs):
    
    data, file_name = sql_nosql_inputs
    with open(file_name, 'w') as write_file:
        json.dump(data, write_file)
        
def create_item(*user_inputs):
    
    my_list = []
    
    for user_input in user_inputs:
        value = input(user_input)
        my_list.append(value)
    
    return my_list