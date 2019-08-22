""" Common functions for controllers
implement commonly used functions here
"""
import random
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

def generate_record(table):
    table = common.get_table_from_file('model/accounting/items.csv')
    id = common.generate_random(table)
    record = terminal_view.get_inputs(['Month', 'Day', 'Year', 'Type', 'Amount'],"Please provide your personal information")

    record.insert(0,id) 
    return record

def generate_record(table):
    table = common.get_table_from_file('model/accounting/items.csv')
    id = common.generate_random(table)
    record = terminal_view.get_inputs(['Month', 'Day', 'Year', 'Type', 'Amount'],"Please provide your personal information")

    record.insert(0,id) 
    return record