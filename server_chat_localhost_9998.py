import socket
import sys

def server():
    c = socket.socket()
    c.bind((socket.gethostname(),9998))
    c.listen(5)
    clentsocket, addr = c.accept()
    while True:
        #print("start integration")
        msg = input(str("server: " ))
        clentsocket.send(msg.encode())
        #print("msg sent")
        msg = clentsocket.recv(1024)
        print("client: ",msg.decode())
        #msg = c.recv(1000163)
        #print(len(msg))
        #msg = s.recv(4000162)
        #print("recvd",msg.decode())

server
