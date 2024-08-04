'''

File Name :  Task3.py
Subject: Incldues solutions of task 3 in python lecture 6
Task: Create a graphical application in Python Tkinter that asks the user to enter two integers and
      displays their sum
By: Abdelrhman Khaled Sobhi

'''

import tkinter

# Create an Object from tkinter called root
root = tkinter.Tk()
root.title("Calculator")
root.config(border=25)
#This function will be called when the button "calc" pressed to do the action needed, it is action
#is to check the operation entered by the user then do this operation
def action():
    operation = math_op.get()
    input1 = int(num1.get())
    input2 = int(num2.get())
    if operation == 0:
        result.set("The Sum is : {} + {} = {}".format(num1.get(),num2.get(),input1 + input2))
    elif operation == 1:
        result.set("The Sub is : {} - {} = {}".format(num1.get(),num2.get(),input1 - input2))
    elif operation == 2:
        result.set("The Mul is : {} x {} = {}".format(num1.get(),num2.get(),input1 * input2))
    elif operation == 3:
        result.set("The Div is : {} / {} = {}".format(num1.get(),num2.get(),input1 / input2))


num1 = tkinter.StringVar()
num2 = tkinter.StringVar()
result = tkinter.StringVar()
math_op = tkinter.IntVar()

#The Entery where the user enter the first number
tkinter.Label(root, text= "Enter First Number").grid(row = 0, column= 0, pady=10)
tkinter.Entry(root, textvariable = num1).grid(row = 0, column= 1, pady=10)
#The Entery where the user enter the second number
tkinter.Label(root, text= "Enter Second Number").grid(row = 1, column= 0, pady=10)
tkinter.Entry(root, textvariable = num2).grid(row = 1, column= 1 , pady=10)
#The label where the output should be printed
tkinter.Label(root, text = "", textvariable = result).grid(row = 2 , column= 1 , pady=10)
#The button used for submit the calculation process
tkinter.Button(root, text="Calc" , width= 25 , command= action ).grid( row = 3 , column= 1, pady=10)
#The radio button used to determine the operation
tkinter.Radiobutton(root, text="Sum", variable= math_op ,value= 0 ).grid( row = 3 , column= 0, pady=10)
tkinter.Radiobutton(root, text="Sub", variable= math_op ,value= 1 ).grid( row = 4 , column= 0, pady=10)
tkinter.Radiobutton(root, text="Mul", variable= math_op ,value= 2 ).grid( row = 5 , column= 0, pady=10)
tkinter.Radiobutton(root, text="Div", variable= math_op ,value= 3 ).grid( row = 6 , column= 0, pady=10)


root.mainloop()