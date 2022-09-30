'''
Write a Python program to get information about the file pertaining to the file mode.

Print the information:
- ID of device containing file
- inode number
- protection
- number of hard links
- user ID of owner
- group ID of owner
- total size (in bytes)
- time of last access
- time of last modification and time of last status change
'''

import os, subprocess

filepath = input("Enter the absolute path of a file you wish to check: ")
info = os.stat(filepath)
inode1 = subprocess.run(['ls', '-il', filepath], stdout=subprocess.PIPE)
inode2 = subprocess.run(['awk', '{print $1}'], stdin=inode1.stdout)


print(f"ID of device containing file: {info.st_dev}")
print(f"inode number: {inode2}")
# print(f"protection: {}")
# print(f"number of hard links: {}")
# print(f"user ID of owner: {}")
# print(f"group ID of owner: {}")
# print(f"total size (in bytes): {}")
# print(f"time of last access: {}")
# print(f"time of last modification and time of last status change: {}")