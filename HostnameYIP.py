import socket
import os
if os.name == 'nt':
    print('1: Apagar el ordenador en un cierto tiempo' + '\n' + '2: Anula el apagado del ordenador' + '\n' + '3: Ip y Hostname' + '\n' + '4: Ping a una dirección ip concreta')
    program = int(input('Que programa quieres ejecutar?'))
    if program == 1:
        tiempoEnSegundos = int(input('En cuanto tiempo quieres apagar el ordenador?'))
        os.system('shutdown -s -t {}'.format(tiempoEnSegundos))
    if program == 2:
        os.system('shutdown -a')
    if program == 3:
        print('El nopmbre del equipo és: {}'.format(socket.gethostname()))
        print('La IP del equipo és: {}'.format(socket.gethostbyname(socket.gethostname())))
    if program == 4:
        print('La IP del equipo és: {}'.format(socket.gethostbyname(socket.gethostname())))
        IPdestino = input('Elije a que IP quieres hacer Ping')
        print(os.system('Ping {}'.format(IPdestino)))

