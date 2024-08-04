'''

File Name :  Task5_func.py - V1
Subject: Incldues solutions of task 5 in python lecture 6
Task: Create server receive multiple clients and keep alive
By: Abdelrhman Khaled Sobhi

'''

'''
This file includes the function Server_Up to start the server and receive multiple clients, and 
the function Server_Handle to handle each client,using threads allowing the server to receive multiple 
clients each client on individule thread this technique is called multithreaded server.
'''
import socket
import threading

'''
Functoin Name: Server_Up():
Subject: this function is used to start the server and receive multiple clients
Parameters: none
Returns: none

''' 
def Server_Up():
    #Initialize the server with TCP protocol and IPv4 address.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Get the server ip and port
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 5000
    #Bind the server to the ip and port
    server.bind((server_ip, server_port))
    #Start the server with 5 disabled connections, an print that server is up
    server.listen(5)
    print("Server is up and running on port {}".format(str(server_port)))

    #Enter the while loop in hte main thread to receive multiple clients
    while True:
        #Wait until a client connect then accept the client, after accepting print that client is connected
        client, address = server.accept()
        print("Client is connected")
        '''
        1- Start a new thread to handle each client, this will allow the server to receive multiple clients 
           and each client on individule thread that achieves the multithreaded server.

        2- While the server accept the client, the client automatically become a thread and call the 
           server handle function to handle the client connection with the srever.
        '''
        client_thread = threading.Thread(target = Server_Handle, args=(client, address))
        '''
        - Set the thread as a daemon thread, ensuring it runs in the background and does not block the 
          program from exiting if the main thread finishes.
        - it is not strictly necessary for the functionality of the server, but it affects the behavior of 
          the threads in relation to the main program.  
        - With this line the server can exit immediately when the main thread finishes or if the program is 
          terminated, even if there are active client threads.  
        '''
        client_thread.daemon = True
        #Start the thread for each client
        client_thread.start()

'''
Functoin Name: Server_Handle(client, address):
Subject: this function is used to handle each client on individule thread.
Parameters: client ip and client port
Returns: none

''' 
def Server_Handle(client, address):
   '''
   The client enters this function automatically when server accept the client and 
    print that client is connected, to make a server able to receive multiple clients 
    and differentiate between them.
   '''
   print("Client ({},{}) is connected".format(str(client),str(address)))

   #Enter the while loop in the thread to receive messages from the client
   while True:
       #Receive the message from the client and print it
       client_msg = client.recv(1024).decode('utf-8')
       print("Client ({},{}) says : {}".format(str(client),str(address),str(client_msg)))
       #Enter the input and send it to the client
       server_send = input("Server says : ")
       server_send_encode = server_send.encode('utf-8')
       client.send(server_send_encode)

   