from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("enter a message")
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddr = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()