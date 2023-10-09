import socket
import random
import time

server_ip = '192.168.88.1'
server_port = 3000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server mendengarkan di {server_ip}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Menerima koneksi dari {client_address}")

    data = client_socket.recv(1024).decode()
    print(f"Data yang diterima dari klien: {data}")

    client_socket.close()
