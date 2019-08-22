# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common

def generate_record(table):
    table = common.get_table_from_file('model/accounting/items.csv')
    id = common.generate_random(table)
    record = terminal_view.get_inputs(['Month', 'Day', 'Year', 'Type', 'Amount'],"Please provide your personal information")

    record.insert(0,id) 
    return record


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.
    Returns:
        None
    """

    table_headers = ['ID', 'Month', 'Day', 'Year', 'Type', 'Amount']
    choice = None
    
    while choice != "0":
        choice = terminal_view.get_choice(['Add', 'Remove', 'Update'])
        table = common.get_table_from_file('model/accounting/items.csv')
        if choice[0] == "1":
            terminal_view.print_table(table, table_headers)
            record = generate_record(table)
            accounting.add(table, record)
            terminal_view.print_table(table, table_headers)
        
        elif choice[0] == "2":
            terminal_view.print_table(table, table_headers)
            id = terminal_view.get_inputs(["ID"], "Please insert ID:")
            accounting.remove(table, id[0] )
            terminal_view.print_table(table, table_headers)
        elif choice == "3":
            terminal_view.print_table(table, table_headers)
            id = terminal_view.get_inputs(["ID"], "Please insert ID:")
            record = record = terminal_view.get_inputs(['Month', 'Day', 'Year', 'Type', 'Amount'],"Please provide your personal information")

            record.insert(0,id[0])
            accounting.update(table, id[0], record)
            terminal_view.print_table(table, table_headers)
#        elif choice == "4":
#            accounting_controller.run()
#        elif choice == "5":
#            sales_controller.run()
#        elif choice == "6":
#            crm_controller.run()
#        else:
#            terminal_view.print_error_message("There is no such choice.")