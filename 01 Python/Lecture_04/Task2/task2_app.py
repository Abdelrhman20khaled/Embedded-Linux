'''

File Name :  task2_app.py
Subject: Incldues solutions of task 2 in python lecture 4
Task: write a Python program to count the Number of words in a
      file.
By: Abdelrhman Khaled Sobhi

'''
#Use with statement to open the file, and it is automatically closed, assign name to "about.txt"
#as file, read the file line by line and count the number of lines
with open("about.txt") as file:
    #"file.read()" will return the data in the file in string format, then we can operate on it
    #as a string by using split() function
    read_file = file.read()
#print the number of words
print("Num of Words in the File is {} Words".format(len(read_file.split())))
