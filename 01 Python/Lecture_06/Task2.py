'''

File Name :  Task2.py
Subject: Incldues solutions of task 2 in python lecture 6
Task: Write a program that asks the user to type and return him its reverse a word
By: Abdelrhman Khaled Sobhi

'''

import tkinter

#Create a root to hold the label and Entry
window = tkinter.Tk()
window.title("Reverse Word")
window.geometry("500x300")

#The Function will be called when the button is pressed to reverse the string
def action():
    user_input = word.get()
    rev_word.set(user_input[::-1]) 

#Create a variable to hold the entry
word = tkinter.StringVar()
rev_word = tkinter.StringVar()

tkinter.Label(window, text="Enter Word").grid(row=0, padx=10, pady=10)
tkinter.Entry(window, textvariable= word).grid(row=0, column=1)
#This label used for print the reverse word
tkinter.Label(window, text = rev_word , textvariable = rev_word, font=("Courier", 15)).grid(row=1, column=1, pady=5)

tkinter.Button(window, text="Submit", command= action).grid(row=2, column=1, pady=5)



window.mainloop()