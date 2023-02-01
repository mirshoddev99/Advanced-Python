import socket
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
SERVER_ADDRESS = (HOST, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen()

clients = []
nick_names = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nick_names[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nick_names.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nick_names.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening...")
receive()
