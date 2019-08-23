""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    price_list = []
    min_price = 100000
    list_of_lowest_price_items = []
    list_of_titles = []
    for line in table:
        price = int(line[2])
        price_list.append(price)
    for price in price_list:
        if price < min_price:
            min_price = price #get the min price from data file
    for line in table:          
        if int(line[2]) == min_price:
            list_of_lowest_price_items.append(line) #list of records with min price
    for line in list_of_lowest_price_items:        
        title = line [1]
        list_of_titles.append(title)
        the_max_title_we_are_looking_for = max(list_of_titles) # the last title in alpha.
    for line in table:
        if line[1] == the_max_title_we_are_looking_for:
            return line[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    date_from = common.convert_to_date(year_from, month_from, day_from)
    date_to = common.convert_to_date(year_to, month_to, day_to)
    list_of_items_sold_in_dates = []
    for line in table:
        year = int(line[5])
        month = int(line[3])
        day = int(line[4])
        date_of_item_sold = common.convert_to_date(year, month, day)
        if date_from < date_of_item_sold and date_of_item_sold > date_to:
            list_of_items_sold_in_dates.append(line)
    return list_of_items_sold_in_dates
