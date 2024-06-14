'''

File Name :  task2.py
Subject: Incldues solutions of task 2 in python
Task: Write a Python program to test whether a passed letter is a vowel or not
By: Abdelrhman Khaled Sobhi

'''
#Receive the input from the user 
my_char = input("Enter the character: ")
#Put the Vowel String that we should serach the input char in it 
Vowel_L = "aieou"
#if the input char in 'aieou' or in 'AIEOU' it will print that is Vowel
if (my_char in Vowel_L) or (my_char in Vowel_L.upper()):
    print("Your Char is Vowel")
else :
    print("Your Char is not Vowel")   

