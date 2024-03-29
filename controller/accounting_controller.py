# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common




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
    filename = 'model/accounting/items.csv'
    columns_headers = ['Month', 'Day', 'Year', 'Type', 'Amount']
    ask_information = "Please provide your personal information"
   
    common.print_art(0)
    while choice != "0":
        choice = terminal_view.get_submenu_choice(['Add', 'Remove', 'Update', 'Which year has the highest profit?',\
            'What is the average (per item) profit in a given year?'])
        table = common.get_table_from_file(filename)
        
        if choice[0] == "1":
            common.clear_terminal()
            common.adding(table, table_headers, filename, columns_headers, ask_information)
        elif choice[0] == "2":
            common.clear_terminal()
            common.removing(table, table_headers,  id, filename)
        elif choice == "3":
            common.clear_terminal()
            common.updating(table, table_headers, id, filename, columns_headers, ask_information)        
        elif choice == "4":
            common.clear_terminal()
            terminal_view.print_table(table, table_headers)
            accounting_result = accounting.which_year_max(table)
            terminal_view.print_result("The year with the highest profit is: ", accounting_result)
        elif choice == "5":
            common.clear_terminal()
            terminal_view.print_table(table, table_headers)
            year = terminal_view.get_inputs(['Year'], 'Which year?')
            result = accounting.avg_amount(table, int(year[0]))
            terminal_view.print_result('The average profit (per item) in a given year is/are: ', result)
        elif int(choice) >= 6:
            common.clear_terminal()
            terminal_view.print_error_message("There is no such choice.")