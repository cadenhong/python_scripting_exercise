'''
Find ASCII Charcode of Inverse Case Character

Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

Examples
Given that:
- "A" char code is: 65
- "a" char code is: 97

counterpartCharCode("A") ➞ 97
counterpartCharCode("a") ➞ 65

Notes
The argument will always be a single character.
Not all inputs will have a counterpart (e.g. numbers), in which case return the input's char code.
'''

def counterpartCharCode(input):
    if len(input) != 1:
        return "Invalid input! Must be a single character long"
    else:
        return ord(input.swapcase())

print(counterpartCharCode("A"))
print(counterpartCharCode("a"))