'''
Write a Python program to convert Python dictionary object (sort by key) to JSON data.
Print the object members with indent level 4.
'''

import json

python_dict = {
    "first" : "Caden",
    "last" : "Hong",
    "career" : "DevOps"
    }

json_data = json.dumps(python_dict, sort_keys=True, indent=4)

print(json_data)

'''
Sample Code:

import json

j_str = {'4': 5, '6': 7, '1': 3, '2': 4}

print("Original String:")
print(j_str)

print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))
'''