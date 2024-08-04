'''

File Name :  task1_sol1.py
Subject: Incldues solutions of task 1 in python lecture 3
Task: Using PyAutoGUI
                - To open vscode
                - install clangd from extension
                - install c++ testmate from extension
                - install c++ helper from extension
                - install cmake from extension
                - install cmake tools from extension
By: Abdelrhman Khaled Sobhi

'''
'''
This script is dependent on your environment.
Before running the script, please ensure the following:

1- Screen Resolution: Confirm your screen's x and y dimensions with pyautogui.position().
2- Internet Connection: Ensure a stable internet connection to avoid issues caused by short delays.
3- Delay Adjustments: If all specifications are confirmed, you may reduce the delay intervals.

'''
import pyautogui as py
from time import sleep

#This shortcut will open the VS code editor, if you run script from external terminal
sleep(3)
py.typewrite('code .')
sleep(1)

# You can modify the list according to your needs
ext_needed = ['clangd', 'c++ testmate', 'c++ helper', 'cmake', 'cmake tools']

#loop on all elements in the list
for i in ext_needed:
    #This shortcut will open the extension screen 
    py.hotkey('ctrl', 'shift', 'x')
    sleep(1 )       
    #This shortcut will delete any thing in search bar 
    py.hotkey('ctrl', 'a', 'delete')
    sleep(1)
    #Write the elements in the list  
    py.typewrite(i)
    sleep(3)
    #Constant method to open chosse the extension you need  
    py.press('tab',presses=2)
    sleep(1)
    py.press('down')
    sleep(1)
    py.press('enter')
    sleep(1)
    # According to my screen the Positon of install button 
    py.click(2525,323, button='left', duration=0.5)
    sleep(1)
    # Delay bewteen installing each element in the list
    sleep(1)

#print done message if task is done
print('All Extensions are installed successfully')