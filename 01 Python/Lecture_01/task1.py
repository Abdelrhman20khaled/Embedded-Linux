'''

File Name :  task1.py
Subject: Incldues solutions of task 1 in python
Task: Write a Python program to count the number 4 in a given list.
By: Abdelrhman Khaled Sobhi

'''
#Create a random list for checking the Number
random_list = [1,2,3,4,5,6,4,6,4,4,5,6,7,7,4,4,4]
# Use built in function 'count' that will count how manny that the argument reapeated
num_of_count = random_list.count(4)
#print the number of count
print("Number 4 Was Repeated {}".format(num_of_count)+" Times")        

# Another Generic Solution
#
#print("Enter the number you want to serach : ")
#my_mun = int(input())
#
#random_list = [1,2,3,4,5,6,4,6,4,4,5,6,7,7,4,4,4]
#num_of_count = random_list.count(my_mun)
#
#print("Number {} Was Repeated {}".format(my_mun,num_of_count)+" Times")  