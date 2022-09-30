'''
String to Integer and Vice Versa

Write two functions:
to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.

Examples
to_int("77") ➞ 77
to_int("532") ➞ 532
to_str(77) ➞ "77"
to_str(532) ➞ "532"
'''

def to_int(str):
    return int(str)

def to_str(int):
    return str(int)


print(type(to_int("77")))
print(type(to_int("532")))
print(type(to_str(77)))
print(type(to_str(532)))