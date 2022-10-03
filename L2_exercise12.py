'''
Friday the 13th

Given the month and year as numbers, return whether that month contains a Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True
has_friday_13(10, 2017) ➞ True
has_friday_13(1, 1985) ➞ False

Notes
January will be given as 1, February as 2, etc ...
'''

from datetime import datetime
from calendar import monthrange

def has_friday_13(month, year):
    numOfDays = monthrange(year, month)[1]
    fridays = []

    for day in range(1, numOfDays+1):
        x = datetime(year, month, day)
        if x.strftime("%A") == "Friday" and day == 13:
            fridays.append(x)

    if len(fridays) == 0:
        return False
    else:
        return True

print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
print(has_friday_13(6, 2020))
print(has_friday_13(5, 2022))


'''
Sample Code:

import calendar

def has_friday_13(month, year):
    return calendar.weekday(year, month, 13) == 4
'''