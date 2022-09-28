'''
Write a Python program to join one or more path components together
and split a given path in directory and file.
'''

def join_path(*arguments):
    joined = ""
    for component in arguments:
        joined+=component
        joined+="/"
    return joined

def split_path(path):
    return path.split('/')

print(join_path("caden","desktop","documents","kura","lectures"))
print(split_path("home/ubuntu/downloads/lecture/name.txt"))


'''
Sample Code: 

import os
path = r'g:\\testpath\\a.txt'
print("Original path:")
print(path)
print("\nDir and file name of the said path:")
print(os.path.split(path))
print("\nJoin one or more path components together:")
print(os.path.join(r'g:\\testpath\\','a.txt'))
'''