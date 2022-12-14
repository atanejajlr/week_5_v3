import time
from utils import read_dictlist, dump_json, print_items_formatted
from operations import get_status_types, get_main_menu, get_main_menu_opts, \
get_item_menu, get_item_menu_opts
from mysqlops import delete_execute, get_item_query, orders_result, read_cafe_database, check_populate_database, \
    insert_execute, update_execute, process_order, price_summary
from mysqlutils import create_connection, read_from_db
import sys, os


def main():
    
    """
    This is the main workflow. This function is called recursively. 
    The application will close only when the user asks for exit in the main menu options.
    This happens in the function get_main_menu_opts
    The code is generic whether you're using a NoSQL (JSON database)
    or an RDBMS SQL database.
    
    """
    
   
    mysql_connection = create_connection()
    cafe_database = read_cafe_database(mysql_connection)
    user_output_orders = read_from_db(orders_result, mysql_connection)
    price_summary_orders = read_from_db(price_summary, mysql_connection)
    user_option = get_main_menu() 
    item_opts_possible = get_main_menu_opts(user_option, cafe_database[0], cafe_database[1], 
                    user_output_orders, check_populate_database, mysql_connection, cafe_database) 
    crud_option = get_item_menu(item_opts_possible[0])
    get_item_menu_opts(crud_option, item_opts_possible, mysql_connection,
        user_option, insert_execute, update_execute, delete_execute, cafe_database, process_order, price_summary_orders)
   
    print("Thanks! You will now be taken back to the main selection options")
    time.sleep(2)
    main()
    
        
if __name__ == "__main__":
    
    main()
    
    
    
    
        
        
    
    

    



        

    
    
    
    
    


    
    
    
    
    