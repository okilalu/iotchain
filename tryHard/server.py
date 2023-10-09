import socket
import random

server_ip = '192.168.88.1'
server_port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)

print('Node is running and waiting for connections...')

while True:
    try:
        client_socket, client_address = server_socket.accept()
        print('Connected to client:', client_address)

        message = client_socket.recv(1024).decode()
        print('Received data:', message)

        response = 'Node received the data'
        client_socket.send(response.encode())

    except:
        if (client_socket.close):
            print("Connection has been stopped")
            print("Error while receive data")

    client_socket.close()
