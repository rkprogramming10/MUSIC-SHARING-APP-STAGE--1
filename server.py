import socket
from threading import Thread
# import time


BUFFER_SIZE = 4096
clients = {}
IP_ADDRESS = '127.0.0.1'
PORT = 8000
SERVER = None


# def handleShowList(client):
#     global clients
#     counter = 0
#     for c in client:
#         counter += 1
#         client_address = clients[c]['address'][0]
#         connected_with = clients[c]['connected_with']
#         message = ''
#         if connected_with:
#             message = f'{counter}. {c} {client_address} connected with {connected_with}, tiul,\n'
#         else:
#             message = f'{counter}. {c} {client_address}, Availabe, tiul,\n'
#         client.send(message.encode())
#         time.sleep(1)


# def handle_message(client, message):
#     if message == 'show list':
#         handleShowList(client)


# def handle_client(client, client_name):
#     global clients, BUFFER_SIZE, SERVER
#     banner1 = 'Welcome you are connected to server\nClick on refresh to see all availabe Users\nSelect the user and click on connect to start chatting'
#     client.send(banner1.encode())

#     while True:
#         try:
#             BUFFER_SIZE = clients[client_name]['file_size']
#             chunk = client.recv(BUFFER_SIZE)
#             message = chunk.decode().strip().lower()
#             if message:
#                 handle_message(client, message)

#         except:
#             pass


def accept_connection():
    global SERVER, clients
    while True:
        client, addr = SERVER.accept()
        print(client, addr)
        # client_name = client.recv(4096).decode().lower()
        # clients[client_name] = {
        #     'client': client,
        #     'address': addr,
        #     'connected_with': '',
        #     'file_name': '',
        #     'file_size': 4096,
        # }
        # print(f'\t\t\t\t{client_name} connected with {addr}')
        # thread = Thread(target=handle_client, args=(client, client_name))
        # thread.start()


def setup():
    print('\n\t\t\t\tIP MESSENGER\n')
    global SERVER, PORT, IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)
    print('\t\t\t\tServer is waiting for incoming connection\n')
    accept_connection()


setup_thread = Thread(target=setup)
setup_thread.start()
