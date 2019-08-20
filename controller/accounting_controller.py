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

    print (
    """\n     Acounting menu \n
    -------------------------\n
    [1] Add new record 
    [2] Remove record 
    [3] Update record
    [4] Which year has the highest profit?
    [5] What is the average (per item) profit in a given year? [(profit)/(items count)]
    [0] Back to main menu
    """)

run()
