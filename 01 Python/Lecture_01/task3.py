'''

File Name :  task3.py
Subject: Incldues solutions of task 3 in python
Task: Write a python program to access environment variables
By: Abdelrhman Khaled Sobhi

'''

'''
Environment Variables:  
are key-value pairs used by operating systems and applications to store configuration settings. 
These variables provide a way to influence the behavior of processes and the software environment 
in which they run.

Examples
PATH: specifies directories where executable programs are located.
HOME: stores the path to the user's home directory.
TEMP or TMP: Path to the directory used for temporary files.
USER or USERNAME: The current logged-in user.
LANG: Defines the language and locale settings.

All of Environment Variables can used by OS Module

'''

import os 

Environment_Variables_Path = os.environ.get("PATH")
Environment_Variables_HOME = os.environ.get("HOME")
Environment_Variables_Temp = os.environ.get("TEMP")
Environment_Variables_User = os.environ.get("USER")
Environment_Variables_Language = os.environ.get("LANG")

print("Path: "+Environment_Variables_Path)
print("Home: "+Environment_Variables_HOME)
print("Temp: "+str(Environment_Variables_Temp))
print("User: "+Environment_Variables_User)
print("Language: "+Environment_Variables_Language)