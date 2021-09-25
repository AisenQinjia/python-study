from socket import *
# serverName = "172.17.61.16" //for wsl
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
# clientSocket.bind(('',5432))
message = input("enter a message")
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddr = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()