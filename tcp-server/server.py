from socket import *
serverport=12001
serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(('',serverport))
serversocket.listen(1)
print('the server is ready to listen')
while True:
    connectionSocket,addr = serversocket.accept()
    message = connectionSocket.recv(1024).decode()
    print('recved message: ' +  message)
    modifedMessage = message.upper()
    connectionSocket.send(modifedMessage.encode())