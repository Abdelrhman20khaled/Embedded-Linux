'''

File Name :  Alexa_Func.py --> Version (1.0)
Subject:This script implements a basic voice assistant functionality using speech recognition,
        text-to-speech conversion, and interaction with external APIs for tasks like retrieving
        current date, time, and location information.
By: Abdelrhman Khaled Sobhi

'''
'''
Note:
    1- It is not the last version, it is a work in progress and more updates will be added.
    2-First you should import some of the libraries you need, some of this libraries may not be
    installed by default, so you should install them first by write pip install <library name>.
    
'''
'''
"speech_recognition" : Library for speech recognition.
"pyautogui" : Used for controlling the mouse and keyboard.
"pyttsx3"   : Text-to-speech conversion library.
"requests"  : Library for making HTTP requests.
"datetime"  : Module for manipulating dates and times.
"time.sleep": Used to delay execution for a given number of seconds
'''
import speech_recognition
import pyautogui
import pyttsx3
import requests
import datetime
from time import sleep
import datetime

'''
Functoin Name: Alexa_Listening():
Subject: Initializes a speech recognizer and listens for speech input from the microphone.
Parameters: None
Returns: text - Recognized text from speech input

'''
def Alexa_Listening():
 recognition = speech_recognition.Recognizer()
 with speech_recognition.Microphone() as voice_source:
        print("Speak Anything :")
        recognition.adjust_for_ambient_noise(voice_source)
        voice_data = recognition.listen(voice_source)
        text = recognition.recognize_google(voice_data, language='en-US')
        return text

'''
Functoin Name: Alexa_Speak(text):
Subject: Converts text to speech and speaks it.
Parameters: text - Text to be converted to speech
Returns: none

''' 
def Alexa_Speak(text): 
    response = pyttsx3.init()
    #response.setProperty('rate', 150)
    response.say(text)
    response.runAndWait()

'''
Functoin Name: Alexa_Response(voice_data):
Subject: Processes the voice input and provides appropriate responses.
Parameters: voice_data - Recognized text from speech input.
Returns: none

''' 
def Alexa_Response(voice_data):
    if ('good morning' in voice_data) or ('hello' in voice_data) or ('hi' in voice_data):
        Alexa_Speak("Good Morning User, How Can I assist you Today?")

    elif ('date' in voice_data) or ('calender' in voice_data):
        get_data = datetime.date()
        print("The date of the Day is {}".format(get_data))   
        Alexa_Speak(get_data)

    elif ('time' in voice_data) or ('hour' in voice_data):
        get_data = datetime.time()
        print("The time now is {}".format(get_data)) 
        Alexa_Speak(get_data)

    elif ('location' in voice_data) or ('zone' in voice_data) or ('city' in voice_data):
        get_ip = requests.api("https://api.ipify.org/?format=json")
        my_ip = get_ip.json()['ip']
        get_data = requests.api.get("https://ipinfo.io/{}/geo".format(my_ip))
        my_city = get_data.json()['city']
        my_country = get_data.json()['country']
        my_location = get_data.json()['loc']
        my_timezone = get_data.json()['timezone']
        print("Your City is {}".format(my_city))
        print("Your Country is {}".format(my_country))
        print("Your Location is {}".format(my_location))
        print("Your Timezone is {}".format(my_timezone))
        Alexa_Speak("Your City is {} Your Country is {} Your Location is {} Your Timezone is {}".format(my_city, my_country, my_location, my_timezone))
        