#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 31201
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
successHeader = "HTTP/1.1 200 OK\r\nContent-Type: text/html;charset=utf-8\r\n\r\n"
failHeader = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024).decode()
        print('recv request: '+ message) 
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read()
        #Send one HTTP header line into socket
        for i in range(0,len(successHeader)):
            connectionSocket.send(successHeader[i].encode()) 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        for i in range(0,len(failHeader)):
            connectionSocket.send(failHeader[i].encode()) 
        #Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 