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
    # modifedMessage = message.upper()
    # connectionSocket.send(modifedMessage.encode())
    break
# google localhost:12001 请求:
# recved message: GET / HTTP/1.1
# Host: localhost:12001
# Connection: keep-alive
# sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
# sec-ch-ua-mobile: ?0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Sec-Fetch-Site: cross-site
# Sec-Fetch-Mode: navigate
# Sec-Fetch-User: ?1
# Sec-Fetch-Dest: document
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6