# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    table_headers = ['ID','Name', 'Birth Year']
    choice = None
    filename = 'model/hr/persons.csv'
    columns_headers = ['Name', 'Birth Year']
    ask_information = "Please provide your personal information"
   
    common.print_art(0)
    while choice != "0":
        choice = terminal_view.get_submenu_choice(['Add', 'Remove', 'Update', 'Get oldest person', 'People closest to average age'])
        table = common.get_table_from_file(filename)
        
        if choice[0] == "1":
            common.clear_terminal()
            common.adding(table, table_headers, filename, columns_headers, ask_information)
        elif choice[0] == "2":
            common.clear_terminal()
            common.removing(table, table_headers,  id, filename)
        elif choice == "3":
            common.clear_terminal()
            common.updating(table, table_headers, id, filename, columns_headers, ask_information )
        elif choice == "4":
            common.clear_terminal()
            terminal_view.print_table(table, table_headers)
            hr_result = hr.get_oldest_person(table)
            terminal_view.print_result("\nThe oldest people are/ person is", hr_result)
        elif choice == "5":
            common.clear_terminal()
            terminal_view.print_table(table, table_headers)
            closest_to_average_people = hr.get_persons_closest_to_average(table)
            terminal_view.print_result("People closest to average age: ", closest_to_average_people)

        elif int(choice) >= 6:
            common.clear_terminal()
            terminal_view.print_error_message("There is no such choice.")        
