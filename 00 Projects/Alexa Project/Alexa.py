'''

File Name :  Alexa.py 
Subject: Alexa Application Project
By: Abdelrhman Khaled Sobhi

'''

import Alexa_Func

while True:

    Voice_Data = Alexa_Func.Alexa_Listening()
    print("you said {}".format(Voice_Data))
    Alexa_Func.Alexa_Response(Voice_Data)


