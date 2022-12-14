'''
Adding Numbers

Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"
add("10", "80") ➞ "90"
add("", "20") ➞ "Invalid Operation"

Notes
If any input is "" or None, return "Invalid Operation".
'''

def add(str1, str2):
    if str1 == None or str2 == None or str1 == "" or str2 == "":
        return "Invalid Operation"
    else:
        return str(int(str1) + int(str2))

print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))

'''
Sample Code:

def add(a,b):
    try: return str(int(a)+int(b))
    except: return "Invalid Operation"
'''