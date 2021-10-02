from socket import *
import ssl
import base64
def sendAndWaitResp(cs,msg):
    print('send ')
    print(msg)
    if isinstance(msg, str):
        cs.send(msg.encode())
    else:
        cs.send(msg)
    recv= cs.recv(1024).decode()
    print(recv)
mailFrom = ""
mailToAddress = ""
password=base64.b64encode("".encode()) + b"\r\n"
userName = base64.b64encode(mailFrom.encode()) + b"\r\n"
msg="\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"
mialPort = 587
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,mialPort))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
sendAndWaitResp(clientSocket,heloCommand)

#start tls communication
tlsCommand = "starttls\r\n"
sendAndWaitResp(clientSocket,tlsCommand)
ttlClientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
#login
loginCommand = "AUTH LOGIN\r\n"
sendAndWaitResp(ttlClientSocket,loginCommand)
sendAndWaitResp(ttlClientSocket,userName)
sendAndWaitResp(ttlClientSocket,password)

#send a mail

# Send MAIL FROM command and print server response.
fromCommand = "MAIL FROM: <" + mailFrom + ">\r\n"
sendAndWaitResp(ttlClientSocket,fromCommand)
# Send RCPT TO command and print server response.
rcptCommand = 'RCPT TO: <'+ mailToAddress + '>\r\n'
sendAndWaitResp(ttlClientSocket,rcptCommand)
dataCommand = 'DATA\r\n'
sendAndWaitResp(ttlClientSocket,dataCommand)
ttlClientSocket.send(msg.encode())
sendAndWaitResp(ttlClientSocket,endmsg)

# quit
quitCommand = 'QUIT\r\n'
sendAndWaitResp(ttlClientSocket,quitCommand)