from socket import *
import sys
import os

serverport=31201
failHeader = "HTTP/1.1 404 NOT FOUND\r\n\r\n".encode()
# Create a server socket, bind it to a port and start listening
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(('',serverport))
tcpSerSock.listen(10)
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    print("req: " + message)
    # Extract the filename from the given message
    proxyPath = message.split()[1]
    filename = proxyPath.partition("/")[2]
    hostn = filename.partition("/")[0].replace("www.","",1)
    print("filename: " +filename)
    print("hostn: " + hostn)
    if(os.path.dirname(filename)!=""):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    fileExist = "false"
    try:
        # Check wether the file exist in the cache
        f = open(filename, "rb") 
        outputdata = f.read() 
        fileExist = "true"
        print("cache hit!")
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send(outputdata)
        tcpCliSock.send("\r\n".encode()) 
        tcpCliSock.close()
        print('Read from cache: ') 
        print(outputdata) 
    except IOError:
        if fileExist == "false":
            print("cache not hit")
            # Create a socket on the proxyserver
            c = socket(AF_INET,SOCK_STREAM)
            try:
                # Connect to the socket to port 80
                c.connect((hostn,80))
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('rwb', 0) 
                fileobj.write(("GET "+ filename + " HTTP/1.0\r\n").encode()) 
                fileobj.write(("Host: "+ hostn +"\r\n\r\n").encode()) 
                fileobj.flush()
                # Read the response into buffer
                serverResp = fileobj.read()
                print("serverResp: ")
                print(serverResp)
                # Create a new file in the cache for the requested file.
                cacheFile = open(filename, "wb")
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                cacheFile.write(serverResp)
                cacheFile.close()
                tcpCliSock.send(serverResp)
            except Exception as e:
                print("Illegal request %s"%e)
        else:
            print("error while reading cache!")
            # HTTP response message for file not found
            tcpCliSock.send(failHeader)
    # Close the client and the server sockets
    tcpCliSock.close()

                    


