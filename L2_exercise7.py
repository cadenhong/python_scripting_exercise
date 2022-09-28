'''
Write a Python program to access only unique key value of a Python object.
'''

# The same key cannot appear more than once in a collection. If the key appears more than once, only the last will be retained.
pyobj = { "fname": "caden", "lname": "hong", "career": "devops", "fname": "bambi", "lname": "powers", "career":"vet", "fname": "jolie", "lname": "powers", "career": "barista"}
print(pyobj)

for pair in pyobj:
    print(f'{pair} -> {pyobj[pair]}')


'''
Sample Code: 

import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj) 
'''