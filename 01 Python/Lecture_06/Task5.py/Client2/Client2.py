'''

File Name :  Client2.py
Subject: This file is used to connect to the server as a client number 2
Task: Create server receive multiple clients and keep alive.
By: Abdelrhman Khaled Sobhi

'''
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_ip = socket.gethostbyname(socket.gethostname())
server_port = 5000
client.connect((sever_ip, server_port))

while True:
   client_message = input("Client2 said:")
   client_message_encoded = client_message.encode("utf-8")
   client.send(client_message_encoded)

   server_response = client.recv(1024)
   server_response_decoded = server_response.decode("utf-8")
   print("Server said:", server_response_decoded)