import os
import pytest
from unittest.mock import patch
from utils import get_input_ints, read_dictlist, delete_item, create_item
from operations import get_main_menu, get_main_menu_opts, get_item_menu, create_prodids
from orders import update_order
import sys


@patch("builtins.input")
def test_get_input_ints(mock_input):
    
    #assemble
    range_limit = 3
    mock_input.return_value = 2
    expected_result = 2
    
    #act
    actual_result = get_input_ints(range_limit)
    
    #assert 
    assert actual_result == expected_result
 
  
@patch("builtins.input", side_effect=["5z", "1"])  
def test_get_input_ints_exception(mock_input):
    
    #assemble
    range_limit = 3
    expected_result = 1
    
    
    #act
    actual_result = get_input_ints(range_limit)
        
    
    #assert 
    assert actual_result == expected_result
    

@patch("builtins.input", side_effect=["5z", "7", "2"])  
def test_get_input_ints_range(mock_input):
    
    #assemble
    range_limit = 3
    expected_result = 2
    
    
    #act
    actual_result = get_input_ints(range_limit)
        
    
    #assert 
    assert actual_result == expected_result
 
 
@patch("builtins.input")   
def test_get_main_menu(mock_input):
    
    #assemble
    mock_input.return_value = 2
    expected_result = 2
    
    #act
    actual_result = get_main_menu()
    
    #assert
    assert actual_result == expected_result
    
@patch("builtins.input", side_effect=["11z", 5, 2])   
def test_get_main_menu_range(mock_input):
    
    #assemble
    expected_result = 2
    
    #act
    actual_result = get_main_menu()
    
    #assert
    assert actual_result == expected_result
    
   
def test_read_dictlist():
    
    #assemble
  
    file_name = "week4_mini_project/tests/test_data/orders.json"
    expected_result = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", 
                        "customer_phone": "0789887334", "courier": 2, "status": "Preparing", "items": [1, 2]}, 
                        {"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                        "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}]
    
    #act
    actual_result = read_dictlist(file_name)
    
    #assert 
    assert actual_result == expected_result
 
@patch("builtins.input")   
def test_delete_item(mock_input):
    
    #assemble
    item_list = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", 
                        "customer_phone": "0789887334", "courier": 2, "status": "Preparing", "items": [1, 2]}, 
                        {"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                        "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}]


    mock_input.return_value = 0
    expected_result = [{"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                        "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}]
    
    #act
    actual_result = delete_item(item_list)
    
    #assert
    
    assert actual_result == expected_result
    
@patch('builtins.input', side_effect=["Johny", "", "", 2, "", ""])  
def test_update_order(mock_input):
    
    #assemble
    order_dict = {"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                    "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}
    
    expected_result = {"customer_name": "Johny", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                    "customer_phone": "0789887334", "courier": 2, "status": "Shipped", "items": [1, 3]}
    
    prod_list = [{"name": "Coke Zero", "price": 2.0}, {"name": "Sprite", "price": 1.8}, 
                 {"name": "Diet Lemonade", "price": 2.2}, {"name": "Small Bowl of Chips", "price": "3.4"}, 
                 {"name": "Veggie Burger with Chips", "price": 6.5}]
    
    #act
    actual_result = update_order(order_dict, prod_list)
    
    #assert
    assert expected_result == actual_result
  
@patch("builtins.input")  
def test_get_item_menu(mock_input):
    
    #assemble
    user_selection = "order"
    mock_input.return_value = 4
    expected_result = 4
    
    #act
    actual_result = get_item_menu(user_selection)
    
    #assert
    assert actual_result == expected_result
    
def test_get_main_menu_opts():
    
    #assemble
    user_option = 2
    prod_list = [{"name": "Coke Zero", "price": 2.0}, {"name": "Sprite", "price": 1.8}]    
    courier_list = [{"name": "John", "phone number": "0789887334"}, {"name": "Tim", "phone number": "0789887156"}]
    orders_dictlist = [{"customer_name": "Claire", "customer_address": "Unit 7, 12 High Street, Derby, DE24 8PZ", 
                    "customer_phone": "0789887334", "courier": 3, "status": "Shipped", "items": [1, 3]}]
    
    expected_result = ("courier", "phone number", courier_list)
    #act
    actual_result = get_main_menu_opts(user_option, prod_list, courier_list, orders_dictlist)
    
    #assert
    assert actual_result == expected_result
    
@patch('builtins.input', side_effect=["Diet Lemonade", "2.80"])  
def test_create_item(mock_input):
    
  
  #assemble
  
  options_tuple = ("product", "price")
  expected_result = ["Diet Lemonade", "2.80"]
  
  #act
  
  actual_result = create_item("Input: Name of the new " + options_tuple[0] + " please?\n", \
                        "Input: " + options_tuple[1].capitalize() + " of the new " + options_tuple[0] + " please?\n")  
   
    
  #assert
  
  assert actual_result == expected_result 
  
  
@patch('builtins.input', side_effect=[2, 0])    
def test_create_prodids (mock_input):
    
    #assemble
    prod_list = [{"name": "Coke Zero", "price": 2.0}, {"name": "Sprite", "price": 1.8}, 
                 {"name": "Small Bowl of Chips", "price": 4.80}]
    item_list = [0, 1] 
    expected_result = [0, 1, 2]
    
    #act
    actual_result = create_prodids(prod_list, item_list)
    
    #assert
    assert actual_result == expected_result
    

    
    
    
    
   
    
    