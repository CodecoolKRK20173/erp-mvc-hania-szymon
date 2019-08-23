# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import common


def run():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)"]
    
    common.print_art(0)
    choice = None
    while choice != "0":
        common.clear_terminal()
        common.print_art(0)
        choice = terminal_view.get_choice(options)
        if choice == "1":
            common.clear_terminal()
            store_controller.run()
        elif choice == "2":
            common.clear_terminal()
            hr_controller.run()
        elif choice == "3":
            common.clear_terminal()
            inventory_controller.run()
        elif choice == "4":
            common.clear_terminal()
            accounting_controller.run()
        elif choice == "5":
            common.clear_terminal()
            sales_controller.run()
        elif choice == "6":
            common.clear_terminal()
            crm_controller.run()
        