import socket
import random
import time

server_ip = '192.168.88.1'
server_port = 5000


def send_data_to_servers(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    client_socket.send(message.encode())
    print(f"Send data {message}")

    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    client_socket.close()


if __name__ == '__main__':
    while True:
        lights_on = False
        temperature = 20.0
        humidity = 50.0
        motion_detected = False
        for hour in range(24):
            temperature += random.uniform(-1.0, 1.0)
            humidity += random.uniform(-5.0, 5.0)
            motion_detected = random.choice([True, False])

            if hour >= 6 and hour < 8:
                lights_on = True
            elif hour >= 18 and hour < 22:
                lights_on = True
            else:
                lights_on = False

            if motion_detected:
                temperature += 1.0
                humidity += 10.0

            message = "Time: {:02d}:00, Lights: {}, Temperature: {:.1f}C, Humidity: {:.1f}%, Motion Detected: {}" .format(
                hour, "On" if lights_on else "Off", temperature, humidity, motion_detected)
            send_data_to_servers(message)

            time.sleep(3)
