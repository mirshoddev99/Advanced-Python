import socket

HOST = '192.168.1.100'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

while True:
    communications_socket, address = server.accept()
    print(f"Connected to {address}")
    msg = communications_socket.recv(1024).decode('utf-8')
    print(f"Message from client is {msg}")
    communications_socket.send(f"Got your message! Thank you!".encode())
    communications_socket.close()
    print(f"Connection with {address} ended!")
