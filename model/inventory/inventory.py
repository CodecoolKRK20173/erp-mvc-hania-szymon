""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
from datetime import date
from model import data_manager
from model import common


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    table.append(record)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for record in table:
        if record[0] == id_:
            table.remove(record)

    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    for index in range(len(table)):
        if table[index][0] == id_:
            table[index] = record

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    current_year = int(date.today().year)
    data_list = []
    for records in table:
        if int(records[3] + records[4]) <= current_year:
            data_list.append(records)
    return data_list


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    manuf_avg = {}
    for record in table:
        manufacturer = record[2]
        durability = record[4]
        if manufacturer not in manuf_avg:
            manuf_avg.update({manufacturer: {'sum': 0, 'count': 0}})
        if manufacturer in manuf_avg:
            manuf_avg[manufacturer]['sum'] += int(durability)
            manuf_avg[manufacturer]['count'] += 1

    for i in manuf_avg:
        manuf_avg[i] = round(float(manuf_avg[i]['sum']/manuf_avg[i]['count']), 2)

    return manuf_avg
