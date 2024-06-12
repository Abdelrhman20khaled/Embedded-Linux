''''

File Name :  main.py
Subject: Incldues solutions of task 2 in python lecture 2
Task: display all location data from IP of the device
By: Abdelrhman Khaled Sobhi

'''

from  requests import api
from FavWebSites import Google

#Request the Public IP from Ipify Website
request_ip = api.get("https://api.ipify.org/?format=json")
#Convert JSON Answer to String IP
device_ip = request_ip.json()['ip']
#Print the IP of the Device 
print("Your Device Public IP: ",device_ip)
#Ask a User if Need to Continue or Not
ch_y_n = input("If you ned to display information? [Y/n] ")
#Check if the user Enter Char Y or n only
if ch_y_n == 'Y' or ch_y_n == 'n':
    if ch_y_n == 'Y':
        #If the USr Wnat to Continue Google will be Opened and Display Location Information
        Google("https://ipinfo.io/{}/geo".format(device_ip))
    else:
     exit
else:
   print("Enter a Valid Choice")
