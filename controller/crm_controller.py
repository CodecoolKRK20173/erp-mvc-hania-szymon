# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table_headers = ['ID','Name', 'Email', 'Subscribed']
    choice = None
    filename = 'model/crm/customers.csv'
    columns_headers = ['Name', 'Email', 'Subscribed']
    ask_information = "Please provide your personal information"
   
   
    while choice != "0":
        choice = terminal_view.get_submenu_choice(['Add', 'Remove', 'Update'])
        table = common.get_table_from_file(filename)
        
        if choice[0] == "1":
            common.adding(table, table_headers, filename, columns_headers, ask_information)
        elif choice[0] == "2":
            common.removing(table, table_headers,  id, filename)
        elif choice == "3":
            common.updating(table, table_headers, id, filename, columns_headers, ask_information)
