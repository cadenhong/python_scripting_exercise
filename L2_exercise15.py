'''
RegEx VII-A: Negative Lookbehind

Write a regular expression that will help us count how many bad cookies are produced every day.
You must use RegEx negative lookbehind.

Example
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = "yourregularexpressionhere"
len(re.findall(pattern, ", ".join(lst))) ➞ 2

Notes
You don't need to write a function, just the pattern.
Do not remove import re from the code.
'''

import re

lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = '(?<!good) cookie'
print(len(re.findall(pattern, ", ".join(lst))))


'''
Sample Code:

import re
pattern = "(?<!good) cookie"
'''