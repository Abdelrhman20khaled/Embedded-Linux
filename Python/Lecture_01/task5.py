'''

File Name :  task4.py
Subject: Incldues solutions of task 4 in python
Task: Print the calendar of a given month and year
By: Abdelrhman Khaled Sobhi

'''

import calendar

year = input("Enter the Year: " )
month = input("Enter the Month: ")
#Store the Calender with W and L equal to 0 (Default Size)
days = calendar.month(int(year),int(month),w=0,l=0)
print(days)