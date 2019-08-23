# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table_headers = ['ID','Title', 'Manufacturer', 'Price', 'In Stock']
    choice = None
    filename = 'model/store/games.csv'
    columns_headers = ['Title', 'Manufacturer', 'Price', 'In Stock']
    ask_information = "Please provide your personal information"
   
   
    while choice != "0":
        choice = terminal_view.get_submenu_choice(['Add', 'Remove', 'Update',\
            'How many different kinds of game are available of each manufacturer?',\
                'What is the average amount of games in stock of a given manufacturer?'])
        table = common.get_table_from_file(filename)
        
        if choice[0] == "1":
            common.adding(table, table_headers, filename, columns_headers, ask_information)
        elif choice[0] == "2":
            common.removing(table, table_headers,  id, filename)
        elif choice == "3":
            common.updating(table, table_headers, id, filename, columns_headers, ask_information)
        elif choice == "4":
            terminal_view.print_table(table, table_headers)
            games_count = store.get_counts_by_manufacturers(table)
            terminal_view.print_result('{Manufacturer: count}', games_count)
        elif choice == "5":
            terminal_view.print_table(table, table_headers)
            manufacturer = terminal_view.get_inputs(['Manufacturer'], 'Which manufacturer?')
            games_average = store.get_average_by_manufacturer(table, manufacturer[0])
            terminal_view.print_result('Avarage amount in stock: ', games_average)
        else:
            terminal_view.print_error_message("There is no such choice.")