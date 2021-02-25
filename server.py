import socket
from select import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем сокет
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()
print("Listening")

to_monitor = []


def connection(server_socket):
    print('Before accept from client')
    client_socket, addr = server_socket.accept()
    print('Connection with ', addr)
    to_monitor.append(client_socket)


def send_msg(client_socket):
    print('Before recieve')
    request = client_socket.recv(4096)
    if request:
        response = 'Zdorova'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                connection(sock)
            else:
                send_msg(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
    print('Outside inner while loop')
