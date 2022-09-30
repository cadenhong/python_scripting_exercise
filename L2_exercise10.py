'''
Write a Python program to start a new process replacing the current process.
'''

import os

cmd = ['echo', 'HELLO']
os.execvp(cmd[0], cmd)

'''
Sample Code:

import os
import sys
program = "python"
arguments = ["hello.py"]
print(os.execvp(program, (program,) + tuple(arguments)))
print("Goodbye")
'''