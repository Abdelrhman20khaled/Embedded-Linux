'''

File Name :  task3_app.py
Subject: Incldues solutions of task 3 in python lecture 4
Task: Write a Python program to write a “list” to a file.
By: Abdelrhman Khaled Sobhi

'''
New_Data = ["\n-Iam 22 years old.", "-I search for embedded internship.", "-Iam from Cairo, Egypt."]
#Use with statement to open the file, and it is automatically closed, assign name to "about.txt"
#as file, use "a" to use a file in append mode (that add new data without remove last data).
with open("about.txt", "a") as file:
    #"file.write()" will add the new data to the file, use "\n" to add new data and separate 
    # with new line
    file.write("\n".join(New_Data))
#print that the data was written successfully
print("Data Was Written Successfully")
#open the file and read it for checking that the data was added
open_f = open("about.txt")
print(open_f.read())