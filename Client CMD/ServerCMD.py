import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen()
print('Listenning...')

while True:
    client,adress = s.accept()
    print('Connected to {}'.format(adress))
    message = input('what you want to write on the CMD?')
    client.send(message.encode('ascii'))
    client.close()

