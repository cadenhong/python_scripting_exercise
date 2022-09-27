'''
Write a Python program to check whether a JSON string contains complex object or not.
'''

import json

def check_complexity(obj):
    list = []
    for value in obj:
        list.append(obj[value])
    
    for item in list:
        if type(item) == dict:
            return True
            exit
        else:
            continue
    return False

complex_json_str = '{"name":"John", "age":30, "city":"New York","pets":{"dog":"jolie","cat":"shane"}}'
simple_json_str = '{"name":"John", "age":30}'

complex_py = json.loads(complex_json_str)
simple_py = json.loads(simple_json_str)

print(check_complexity(complex_py))
print(check_complexity(simple_py))


'''
Sample Code: 

import json
def is_complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)
'''