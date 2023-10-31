import socket
from Savoir import Savoir

rpcuser = 'multichainrpc'
rpcpassword = '7iY4yXdDUTyhdzY4SdvP7zir2WvW1BKiFcC5CHx46wan'
rpchost = '192.168.88.1'
rpcport = '2000'
chain_name = 'my-chain-clne'

multichain = Savoir(rpcuser, rpcpassword, rpchost, rpcport, chain_name)

server_ip = "192.168.88.1"
server_port = 4000

addr = (server_ip, server_port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(addr)
server_socket.listen(5)
print(f"Server mendengarkan di {addr}")


def handle_recv_data():
    response = 'Node received the data'
    client_socket.send(response.encode())

    try:
        txid = multichain.publish("iotdata", "key1", data)
        print("Data telah disimpan dengan TXID:", txid)
    except Exception as e:
        print("Error :", e)

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    print("Menerima koneksi dari", client_address)

    data = client_socket.recv(1024).decode()
    print("Menerima data:", data)

    handle_recv_data()
