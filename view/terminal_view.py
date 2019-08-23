""" Terminal view module """



def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    

    from beautifultable import BeautifulTable

    
    
    beautiful_table = BeautifulTable()
    beautiful_table.column_headers = title_list
    for row in table:

        beautiful_table.append_row(row)

    print(beautiful_table)

def print_result(label, result):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """


    value_type_str = isinstance(result, str)
    value_type_dict = isinstance(result, dict)
    value_type_list = isinstance(result, list)

    if value_type_str == True:
        print("☺ ✎ ® \n{}\n {}\n".format(label, result))
    elif value_type_dict == True:
        print("\n",label, ":", "\n"  )
        for key, value in result.items():
            print("♧ ✓ ☺ ", key, "-", value, )
        print("\n")
    elif value_type_list == True:
        print(label, ":" ,"\n")
        for item in result:
            print("⚅ ♔ ♯ ",item)
        print("\n")


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("{}:".format(title))
    
    for i in range(len(list_options)):
        print("({}) {}".format(i+1, list_options[i]))
    print("(0) {}".format(exit_message))
    


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
   
    for item in list_labels:
        inputs.append(input("{}:".format(item) ))

    


    return inputs

def get_choice(options):
    print_menu("Main menu",options, "Exit program")
    inputs = get_inputs(["Please enter a number "], "")
    return inputs[0]

def get_submenu_choice(options):
    print_menu("Menu",options, "Back to Main Menu")
    inputs = get_inputs(["Please enter a number "], "")
    return inputs[0]

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠\nError: {}\n☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠\n".format(message))

