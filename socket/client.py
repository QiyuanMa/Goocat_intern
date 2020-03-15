from socket import socket,AF_INET,SOCK_STREAM

HOST = '127.0.0.1' # or 'localhost'
PORT = 50008
BUFSIZ =4098
ADDR = (HOST,PORT)


while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data1 = input('>')
    #data = str(data)
    if not data1:
        break
    tcpCliSock.send(data1.encode())
    data1 = tcpCliSock.recv(BUFSIZ)
    if not data1:
        break
    print(data1.decode('utf-8'))
    tcpCliSock.close()

