from socket import *
import time 
serverName = "172.17.58.236"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
for i in range(10):
    timeStart = time.time() 
    clientSocket.settimeout(1)
    message = "ping " + str(i)
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    try:
        modifiedMessage,serverAddr = clientSocket.recvfrom(2048)
        timeEnd = time.time() 
        print("recv pong, RTT: " + str((timeEnd-timeStart)))
    except:
        print("lost: " + str(i))