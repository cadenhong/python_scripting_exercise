'''
To the Power of _____

Create a function that takes a base number and an exponent number and returns the calculation.

Examples
calculate_exponent(5, 5) ➞ 3125
calculate_exponent(10, 10) ➞ 10000000000
calculate_exponent(3, 3) ➞ 27

Notes
All test inputs will be positive integers.
Don't forget to return the result.
'''

def calculate_exponent(base, exponent):
    return base ** exponent

print(calculate_exponent(5, 5))
print(calculate_exponent(10, 10))
print(calculate_exponent(3, 3))