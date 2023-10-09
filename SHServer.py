# import socket

# # Define the server IP address and port
# server_ip = '192.168.88.1'
# server_port = 5000

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the IP address and port
# server_socket.bind((server_ip, server_port))

# # Listen for incoming connections
# server_socket.listen(1)

# print('Smart Home Controller is running and waiting for connections...')

# while True:
#     # Accept a client connection
#     client_socket, client_address = server_socket.accept()
#     print('Connected to client:', client_address)

#     # Receive data from the client
#     data = client_socket.recv(1024).decode()
#     print('Received data:', data)

#     # Process the data and control the smart home
#     # Implement your smart home logic here
#     def handle_recv(data):
#         print(data)

#         # Send response back to the client
#         response = 'Smart Home Controller received the data'
#         client_socket.send(response.encode())

#         # Close the connection with the client
#         client_socket.close()

# import socket
# import json

# # Define the server IP address and port
# server_ip = "192.168.88.1"
# server_port = 5000
# HEADER = 4096

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the IP address and port
# server_socket.bind((server_ip, server_port))

# # Listen for incoming connections
# server_socket.listen(1)

# print('Node Admin is running and waiting for connections...')

# while True:
#     # Accept a client connection
#     client_socket, client_address = server_socket.accept()
#     print('Connected to client:', client_address)

#     # Receive data from the client
#     data = client_socket.recv(HEADER).decode("utf-8")
#     print('Received data:', data)

#     try:
#         # Parse the JSON data received from the client
#         data_json = json.loads(data)

#         # Extract information from the JSON data
#         jam = data_json["jam"]
#         lampu_hidup = data_json["lampu"]
#         suhu = data_json["suhu"]
#         kelembaban = data_json["kelembaban"]
#         gerakan_terdeteksi = data_json["gerakan_terdeteksi"]

#         # Implement your smart home control logic here
#         if jam >= 6 and jam < 8:
#             # Nyalakan lampu pada pagi hari
#             lampu_hidup = True
#         elif jam >= 18 and jam < 22:
#             # Nyalakan lampu pada malam hari
#             lampu_hidup = True
#         else:
#             # Matikan lampu pada malam hari
#             lampu_hidup = False

#         # Implement more control logic based on other sensor data if needed

#         # Prepare a response message
#         response_message = f"Jam: {jam:02d}:00, Lampu: {'Hidup' if lampu_hidup else 'Mati'}, Suhu: {suhu:.1f}C, Kelembaban: {kelembaban:.1f}%, Gerakan Terdeteksi: {gerakan_terdeteksi}"

#         # Send the response back to the client
#         client_socket.send(response_message.encode())

#     except json.JSONDecodeError as e:
#         print("Error decoding JSON data:", e)

#     # Close the connection with the client
#     client_socket.close()
