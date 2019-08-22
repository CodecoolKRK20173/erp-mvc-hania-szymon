""" Common functions for controllers
implement commonly used functions here
"""
import random
from view import terminal_view
from model.accounting import accounting
from controller import common
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """


    generated = ''
    list_of_keys = []
    id_part1, id_part_2, id_part3, id_part4 = '', '' , '', ''
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_characters = '!@#$%^&*()?'
    numbers = '1234567890'
    for i in range(len(table)):
        list_of_keys.append(table[i][0])
    #print(list_of_keys)

    id_part1 = id_part1 + random.choice(letters) + random.choice(letters)
    id_part_2 = id_part_2 + random.choice(special_characters) + random.choice(special_characters)
    id_part3 = id_part3 + random.choice(numbers) + random.choice(numbers)
    id_part4 = id_part4 + random.choice(letters) + random.choice(letters)
    
    
    generated = generated + id_part1 + id_part3 + id_part4 + id_part_2
    
    while generated in list_of_keys:
        generated = generated + id_part1 + id_part3 + id_part1 + id_part_2
    
    # your code


    return generated

def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table

def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file

    Returns:
         None
    """
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")

def get_id_from_user():
    id = terminal_view.get_inputs(["ID"], "Please insert ID:")
    return id

def generate_record(table, columns_headers, ask_information, filename):
    table = common.get_table_from_file(filename)
    id = common.generate_random(table)
    record = terminal_view.get_inputs(columns_headers, ask_information)

    record.insert(0,id) 
    return record

def adding(table, table_headers, filename, columns_headers, ask_information):
    terminal_view.print_table(table, table_headers)
    record = generate_record(table, columns_headers, ask_information, filename )
    accounting.add(table, record)
    terminal_view.print_table(table, table_headers)
    common.write_table_to_file(filename, table)

def removing(table, table_headers, id, filename):
    terminal_view.print_table(table, table_headers)
    id = get_id_from_user()
    accounting.remove(table, id[0] )
    terminal_view.print_table(table, table_headers)
    common.write_table_to_file(filename, table)

def updating(table, table_headers, id, filename, columns_headers, ask_information):
    terminal_view.print_table(table, table_headers)
    id = get_id_from_user()
    record = generate_record(table, columns_headers, ask_information, filename)
    accounting.update(table, id[0], record)
    terminal_view.print_table(table, table_headers)
    common.write_table_to_file(filename, table)