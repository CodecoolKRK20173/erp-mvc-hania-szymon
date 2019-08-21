


table = [(0,1,2,2016,'in',50), (0,1,2,2016,'out',10),(0,1,2,2015,'out',20),(0,1,2,2015,'in',30)]

def dupa(table):

    years_profits = {}
    for record in table:
        if record[3] not in years_profits:
            years_profits.update({record[3]: 0})
        if record[4] == 'in':
            years_profits[record[3]] += record[5]
        else:
            years_profits[record[3]] -= record[5]
  
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""

    v = list(years_profits.values())
    k = list(years_profits.keys())
    return int(k[v.index(max(v))])


print(dupa(table))

