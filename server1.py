import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем сокет
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=connection)


def connection(server_socket):
    print('Before from client')
    client_socket, addr = server_socket.accept()
    print('Connection with ', addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_msg)


def send_msg(client_socket):
    print('Before recieve')
    request = client_socket.recv(4096)
    if request:
        response = 'Zdorova'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select() #(key, events) key - SelectorKey object (named tuple) fileobj, events, data
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
    print('Outside inner while loop')
