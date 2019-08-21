""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
    # your code

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

    # your code

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

    # your code

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    name_list = []
    max_characters_in_name = 0
    longest_name = None
    list_of_the_longest = []
    sort_list = []
    for line in table:
        name_from_table = line[1]
        name_list.append(name_from_table) #list of names
    for name in name_list:   
        if len(name) > max_characters_in_name:
            max_characters_in_name = len(name) #Number of characters in longest name
            longest_name = name #the longest name
    for name in name_list:     
        if len (name) == len (longest_name):
            list_of_the_longest.append(name) #the list of longest names
    the_name_we_are_looking_for = max (list_of_the_longest)    
    for line in table:
        if line[1] == the_name_we_are_looking_for:
            return line[0]

            


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    agreed_list = []
    final_list = []
    for line in table:
        agreed_for_emails = line [-1]
        if agreed_for_emails == '1':
            agreed_list.append(line) 
            for person_details in agreed_list:  
                result = '{};{}'.format(person_details[2], person_details[1])
                final_list.append(result)
    return final_list    
