from socket import *
serverport=12000
serversocket=socket(AF_INET,SOCK_DGRAM)
serversocket.bind(('',serverport))
print("go listen")
while True:
    m, ca = serversocket.recvfrom(2048)
    mm = m.decode().upper()
    print("back: " + mm)
    serversocket.sendto(mm.encode(),ca)