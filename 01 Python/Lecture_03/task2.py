'''

File Name :  task2.py
Subject: Incldues solutions of task 2 in python lecture 3
Task: Using “Pyautogui” to open Emails and change Emails from unread to read
By: Abdelrhman Khaled Sobhi

'''

import pyautogui as py
from time import sleep
import webbrowser

# Declare location variable for search about the picture
location = None
#Open the web browser (google chrome >> gmail) and wait for 5 seconds
webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
sleep(5)
#Serach for the picture and wait for 2 seconds, you should change the path of the picture according to your environment
while location is None:
    location = py.locateOnScreen('/home/abdelrahman/Embedded Linux/Pic_Scripts/another_op.png', confidence=0.9)
    sleep(2)
#Click on the picture and wait for 1 second
py.click(location)
sleep(1)
#Press Enter to make all messages read
py.press('enter')
sleep(1)
#Finally print suuccess message if task is done
print("All Emails are opened successfully")

 