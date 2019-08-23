# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table_headers = ['ID','Title', 'Price', 'Month', 'Day', 'Year']
    choice = None
    filename = 'model/sales/sales.csv'
    columns_headers = ['Title', 'Price', 'Month', 'Day', 'Year']
    ask_information = "Please provide your personal information"
   
   
    while choice != "0":
        choice = terminal_view.get_submenu_choice(['Add', 'Remove', 'Update', 'Check lowest price item', 'Check items sold between dates'])
        table = common.get_table_from_file(filename)
        
        if choice[0] == "1":
            common.adding(table, table_headers, filename, columns_headers, ask_information)
        elif choice[0] == "2":
            common.removing(table, table_headers,  id, filename)
        elif choice == "3":
            common.updating(table, table_headers, id, filename, columns_headers, ask_information )
        elif choice == "4":
            terminal_view.print_table(table, table_headers)
            sales_id = sales.get_lowest_price_item_id(table)
            terminal_view.print_result("The lowest price item id is:", sales_id)
        elif choice == "5":
            terminal_view.print_table(table, table_headers)
            date_list = terminal_view.get_inputs(['month_from', 'day_from', 'year_from', 'month_to', 'day_to', 'year_to'], "Please provide dates information: ")
            sold_list = sales.get_items_sold_between(table, int(date_list[0]), int(date_list[1]), int(date_list[2]), int(date_list[3]), int(date_list[4]), int(date_list[5]) )
            terminal_view.print_result("The items sold between given dates are:", sold_list)
        else:
            terminal_view.print_error_message("There is no such choice.")