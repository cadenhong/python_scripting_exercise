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

import os, datetime

filepath = input("Enter the path of a file you wish to check: ")
info = os.stat(filepath)

def secondsToDate(seconds):
    convertedDate = datetime.datetime.fromtimestamp(seconds).strftime("%A, %B %d, %Y, %H:%M:%S")
    return convertedDate

access_seconds = info.st_atime
mod_seconds = info.st_mtime
meta_seconds = info.st_ctime

print()
print(f"ID of device containing file: {info.st_dev}")
print(f"inode number: {info.st_ino}")
print(f"protection: {info.st_mode}")
print(f"number of hard links: {os.stat(filepath).st_nlink}")
print(f"user ID of owner: {info.st_uid}")
print(f"group ID of owner: {info.st_gid}")
print(f"total size (in bytes): {info.st_size}")
print(f"time of last access: {secondsToDate(access_seconds)}")
print(f"time of last modification: {secondsToDate(mod_seconds)}")
print(f"time of last status change: {secondsToDate(meta_seconds)}")


'''
Sample Code:

path = 'e:\\testpath\\p.txt'
fd = os.open(path, os.O_RDWR)
info = os.fstat(fd)
print (f"ID of device containing file: {info.st_dev}")
print (f"Inode number: {info.st_ino}")
print (f"Protection: {info.st_mode}")
print (f"Number of hard links: {info.st_nlink}")
print (f"User ID of owner: {info.st_uid}")
print (f"Group ID of owner: {info.st_gid}")
print (f"Total size, in bytes: {info.st_size}")
print (f"Time of last access: {info.st_atime}")
print (f"Time of last modification: {info.st_mtime }")
print (f"Time of last status change: {info.st_ctime }")
os.close( fd)
'''