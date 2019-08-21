""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    years_profits = {}
    for record in table:
        if record[3] not in years_profits:
            years_profits.update({record[3]: 0})
        if record[4] == 'in':
            years_profits[record[3]] += record[5]
        else:
            years_profits[record[3]] -= record[5]

    """
    Create a list of the dict's keys and values;
    Returns:
    The key with the max value
    """

    v = list(years_profits.values())
    k = list(years_profits.keys())
    return int(k[v.index(max(v))])


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    year_item_count = 0
    year_profit = 0
    for record in table:
        if record[3] == int(year):
            if record[4] == 'in':
                year_item_count += 1
                year_profit += record[5]
            else:
                year_profit -= record[5]
    average = year_profit / year_item_count

    return average


