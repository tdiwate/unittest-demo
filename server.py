import socket
import sys


server_address = ('localhost', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(server_address)

sock.listen(1)

while(True):
    connection, client_address = sock.accept()
    print(connection)
    print(client_address)
    try:
        while(True):    
            data = connection.recv(6)
            if data:
                connection.sendall(data)
            else:
                break;       
    finally:
        connection.close()

