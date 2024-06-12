'''

File Name :  task2.py
Subject: Incldues solutions of task 2 in python
Task: Write a Python program to test whether a passed letter is a vowel or not
By: Abdelrhman Khaled Sobhi

'''

print("Enter the character:")
my_char = input()
flag = 1
Vowel_L = ['A','E','I','O','U','a','e','i','o','u']

for i in Vowel_L:
    if my_char == i:
        flag = 0
        break
    else:
        flag = 1

if flag == 0:
    print("The Char Entered is Vowel")
else:
    print("The Char Entered is Not Vowel")