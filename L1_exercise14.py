'''
Basic Variable Assignment

A student learning Python was trying to make a function.
His code should concatenate a passed string name with string "Edabit" and store it in a variable called result.
He needs your help to fix this code.

Examples
name_string("Mubashir") ➞ "MubashirEdabit"
name_string("Matt") ➞ "MattEdabit"
name_string("python") ➞ "pythonEdabit"

Notes
Don't forget to return the result.
'''

def name_string(name):
    addToEnd = "Edabit"
    newName = name + addToEnd
    return newName


print(name_string("Mubashir"))
print(name_string("Matt"))
print(name_string("python"))