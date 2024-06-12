'''

File Name :  task1.py
Subject: Incldues solutions of task 1 in python
Task: Write a Python program to count the number 4 in a given list.
By: Abdelrhman Khaled Sobhi

'''

random_list = [1,2,3,4,5,6,4,6,4,4,5,6,7,7,4,4,4]
counter = 0
for i in random_list:
    if i==4:
        counter+=1

print("Number 4 Was Repeated {}".format(counter)+" Times")        

# Another Generated Solution

#print("Enter the number you want to serach : ")
#my_mun = int(input())
#
#random_list = [1,2,3,4,5,6,4,6,4,4,5,6,7,7,4,4,4]
#counter = 0
#
#for i in random_list:
#    if i==my_mun:
#        counter+=1
#
#print("Number {} Was Repeated {}".format(my_mun,counter)+" Times")  