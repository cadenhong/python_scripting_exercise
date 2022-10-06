'''
Multiple of 100

Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False.

Examples
divisible(1) ➞ False
divisible(1000) ➞ True
divisible(100) ➞ True
'''

def divisible(num):
    return num % 100 == 0

print(divisible(1))
print(divisible(1000))
print(divisible(100))