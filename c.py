import socket
import time
import random

server_ip = '192.168.88.1'
server_port = 3000


def send_data_to_server(data):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        client_socket.send(data.encode())
        print(f"Kirim Data : {data_simulasi}")

        client_socket.close()
    except Exception as e:
        print("Gagal mengirim data ke server:", str(e))


if __name__ == '__main__':
    while True:
        suhu = random.randint(20, 30)
        kelembaban = random.randint(40, 60)

        data_simulasi = f"Suhu: {suhu}°C, Kelembaban: {kelembaban}%"
        send_data_to_server(data_simulasi)

        time.sleep(5)


# def recv_response():

#     # Membuat socket klien
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((server_ip, server_port))

#     # Receive response from the server
#     response = client_socket.recv(1024).decode("utf-8")
#     print('Received response:', response)
