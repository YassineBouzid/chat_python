import socket
import os
import sys

def recieve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.2.4', 9998))
    while True:
        #print("got connected")
        msg = s.recv(1024)
        print("server:",msg.decode())
        msg2 = input(str("client : " ))
        s.send(msg2.encode())
        #print("msg2 been sent",msg2)
        #s.close()


recieve()