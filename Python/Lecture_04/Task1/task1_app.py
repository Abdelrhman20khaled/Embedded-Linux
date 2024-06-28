'''

File Name :  task1_app.py
Subject: Incldues solutions of task 1 in python lecture 4
Task: Write a Python program to count the number of lines in a
      text file.
By: Abdelrhman Khaled Sobhi

'''
#Use with statement to open the file, and it is automatically closed, assign name to "about.txt"
#as file, read the file line by line and count the number of lines
with open("about.txt") as file:
    #"file.readline()" will return number of lines in list format, then we can operate on it
    #by using len() function
    num_lines = file.readlines()
#print the number of lines
print("Num of Lines in the File is {} Lines".format(len(num_lines)))
