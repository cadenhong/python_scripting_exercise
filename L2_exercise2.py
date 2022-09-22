'''
Write a Python program to convert Python object to JSON data.
'''

import json

python_obj = {
    "first" : "Caden",
    "last" : "Hong",
    "Path" : "DevOps"
    }

json_obj = json.dumps(python_obj)

print(json_obj)


'''
Sample Code: 

import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)

# result is a JSON string:
print(j_data)
'''