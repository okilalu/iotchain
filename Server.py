import socket
import json

# Define the server IP address and port
server_ip = "192.168.88.1"
server_port = 5500

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)

print('Node Admin is running and waiting for connections...')

# Initial state of the smart home
lampu_hidup = False

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Connected to client:', client_address)

    # Receive data from the client
    data = client_socket.recv(4096).decode()
    print('Received data:', data)

    # Process the data and control the smart home
    # Implement your smart home logic here

    try:
        # Parse the JSON data received from the client
        data_json = json.loads(data)

        # Extract information from the JSON data
        suhu = data_json.get("suhu", 0.0)
        gerakan_terdeteksi = data_json.get("gerakan_terdeteksi", False)

        # Implement your smart home logic here
        if suhu > 25.0:
            # Nyalakan lampu jika suhu melebihi 25°C
            lampu_hidup = True
        elif gerakan_terdeteksi:
            # Nyalakan lampu jika ada gerakan terdeteksi, terlepas dari suhu
            lampu_hidup = True
        else:
            # Matikan lampu jika tidak ada gerakan dan suhu di bawah 25°C
            lampu_hidup = False

        # Prepare a response message
        response_message = f"Lampu: {'Hidup' if lampu_hidup else 'Mati'}"

        # Send the response back to the client
        client_socket.send(response_message.encode())

    except json.JSONDecodeError as e:
        print("Error decoding JSON data:", e)

    # Close the connection with the client
    client_socket.close()

    # # Convert data to JSON format
    # data_json = json.dumps(data)

    # # Send response back to the client
    # response = 'Node Admin received the data'
    # client_socket.send(response.encode())
