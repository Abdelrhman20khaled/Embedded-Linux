'''

File Name :  main.py
Subject: Incldues solutions of task 1 in python lecture 2
Task: main uses a module to print avourite websites
By: Abdelrhman Khaled Sobhi

'''
#include FavWebSites Module
from FavWebSites import Google
#Write The Menu in List for more readable
social_list = ['1- Facebook','2- LinkedIn','3- GitHub','4- Instagram']
#loop on list to dispaly it    
for i in range(len(social_list)): 
    print(social_list[i])
# Ask user to chose which link he needs to open
ch = input("Enter the Number: ")
# Check about thr char that user entered
if int(ch) >=1 and int(ch)<=4:
    if int(ch) ==1:
        Google("https://w22.facebook.com")
    elif int(ch) ==2:     
         Google("https://www.linkedin.com/login/ar")
    elif int(ch) ==3:     
         Google("https://www.github.com")
    else:
         Google("https://www.instagram.com/")
else:
     print("Enter Valid Number")
   