# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table_headers = ['ID', 'Name', 'Manufacturer', 'Purchase Year', 'Durability']
    choice = None
    filename = 'model/inventory/inventory.csv'
    columns_headers = ['Name', 'Manufacturer', 'Purchase Year', 'Durability']
    ask_information = "Please provide your personal information"    

    while choice != "0":
        choice = terminal_view.get_submenu_choice(['Add', 'Remove', 'Update', "Items that have not exceeded their durability yet", "Average durability by manufactirers"])
        table = common.get_table_from_file(filename)
        
        if choice[0] == "1":
            common.adding(table, table_headers, filename, columns_headers, ask_information)
        elif choice[0] == "2":
            common.removing(table, table_headers,  id, filename)
        elif choice == "3":
            common.updating(table, table_headers, id, filename, columns_headers, ask_information )
        elif choice == "4":
            terminal_view.print_table(table, table_headers)
            availible_items = inventory.get_available_items(table)
            terminal_view.print_result("Items that have not exceeded their durability yet", availible_items)
        elif choice == "5":
            terminal_view.print_table(table, table_headers)
            average_durability = inventory.get_average_durability_by_manufacturers(table)
            terminal_view.print_result("Average durability by manufactirers:", average_durability)
        else:
            terminal_view.print_error_message("There is no such choice.")
