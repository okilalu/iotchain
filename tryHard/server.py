import socket
import threading

server_ip = "192.168.88.1"
server_port = 4000

addr = (server_ip, server_port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(addr)
server_socket.listen(5)
print(f"Server mendengarkan di {addr}")


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Menerima data:", data)
        response = 'Node received the data'
        client_socket.send(response.encode())
    client_socket.close()


def client_handler():
    while True:
        client_socket, client_address = server_socket.accept()
        print("Menerima koneksi dari", client_address)
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    client_handler()
