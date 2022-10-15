'''
Date Format

Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
format_date("11/12/2019") ➞ "20191211"
format_date("12/31/2019") ➞ "20193112"
format_date("01/15/2019") ➞ "20191501"

Notes
Return value should be a string.
'''

def format_date(dateInput):
    date_components = dateInput.split('/')
    dateOutput = date_components[2] + date_components[1] + date_components[0]
    return dateOutput
    #return ''.join((date_components[2], date_components[1], date_components[0]))

print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))