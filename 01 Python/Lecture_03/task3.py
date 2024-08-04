'''

File Name :  task3.py
Subject: Incldues solutions of task 3 in python lecture 3
Task: Write a Python program to get the command-line arguments
By: Abdelrhman Khaled Sobhi

'''

import sys
# Print the all command line arguments
# if write this commnd "python3 task3.py -m pip show pyautogui"
# if write this commnd "python3 task3.py sudo nano /etc/resolv.conf"
print('Numeber of arguments: '+ str(len(sys.argv)) + ' arguments')
#Print List of all command line arguments
print(sys.argv)