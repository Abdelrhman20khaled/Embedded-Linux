'''

File Name :  Task1.py
Subject: Incldues solutions of task 1 in python lecture 6
Task: Make this specific template of buttons and each button display different name
By: Abdelrhman Khaled Sobhi

'''

import tkinter
import functools

#Create a root to hold the buttons and give it name "Buttons"
root = tkinter.Tk()
root.title("Buttons")
#this function will be called when the button 1 is pressed
def btn1(text):
    print("Button 1 was pressed")
#this function will be called when the button 2 is pressed
def btn2():
    print("Button 2 was pressed")
#this function will be called when the button 3 is pressed
def btn3():
    print("Button 3 was pressed")
#this function will be called when the button 4 is pressed
def btn4():
    print("Button 4 was pressed")
#Add buttons to the root
tkinter.Button(root, text="Button 1", command= btn1).grid(row=0, column=1)
tkinter.Button(root, text="Button 2", command= btn2).grid(row=1, column=0)
tkinter.Button(root, text="Button 3", command= btn3).grid(row=1, column=3)
tkinter.Button(root, text="Button 4", command= btn4).grid(row=2, column=1)
#Display the root
root.mainloop()
#Another Solution
'''
#this function used partial function that can call the same function with different arguments
def callback_btn(button_number):
    print("Button {} was pressed".format(button_number))
#Add buttons to the root
tkinter.Button(root, text="Button 1", command= functools.partial(callback_btn,1)).grid(row=0, column=1)
tkinter.Button(root, text="Button 2", command= functools.partial(callback_btn,2)).grid(row=1, column=0)
tkinter.Button(root, text="Button 3", command= functools.partial(callback_btn,3)).grid(row=1, column=3)
tkinter.Button(root, text="Button 4", command= functools.partial(callback_btn,4)).grid(row=2, column=1)
#Display the root
root.mainloop()
'''