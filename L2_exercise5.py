'''
Write a Python program to convert JSON encoded data into Python objects.
'''

import json

jobj_dict = '{"first": "Caden", "last": "Hong", "job": "DevOps"}'
jobj_list = '["Jolie", "Bambi", "Shane", "Samantha"]'
jobj_string = '"Kura Labs"'
jobj_int = '123'
jobj_float = '45.67'

pyob_dict = json.loads(jobj_dict)
pyob_list = json.loads(jobj_list)
pyob_string = json.loads(jobj_string)
pyob_int = json.loads(jobj_int)
pyob_float = json.loads(jobj_float)

print(pyob_dict) 
print(pyob_list)
print(pyob_string)
print(pyob_int)
print(pyob_float)