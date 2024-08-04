'''

File Name :  Task4.py
Subject: Incldues solutions of task 4 in python lecture 6
Task: Write a program in Python that displays a window to the user that asks them to enter an integer
      N and displays its factorial
By: Abdelrhman Khaled Sobhi

'''

import tkinter
import math

root = tkinter.Tk()
root.title("Factorial")
root.geometry("500x300")

#This function will be called when the button "calc" pressed to do the action needed, it is action
#is to check the operation entered by the user then do this operation
def action():
    input = int(number.get())
    result.set("The Factorial of {} is {}! = {}".format(number.get(),number.get(),math.factorial(input)))

result = tkinter.StringVar()
number = tkinter.StringVar()

tkinter.Label(root, text= "Enter The Number").grid(row = 0, column= 0, padx=50,pady=10) 
tkinter.Entry(root, textvariable= number).grid(row = 0, column= 1, pady=10)   
tkinter.Label(root, text= result , textvariable= result).grid(row = 1, column= 1, pady=10)
tkinter.Button(root, text="Calc" , width= 15 , command= action ).grid( row = 2 , column= 1, pady=10)

root.mainloop()