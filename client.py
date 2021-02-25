import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect(('localhost', 5001))
while True:
    client_socket.send(input().encode())
    responce = client_socket.recv(4096)
    print(responce.decode())
client_socket.close()

