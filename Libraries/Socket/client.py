import socket

HOST = '192.168.1.100'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


client.send("Hello My first Socket Server~~".encode())
received_msg = client.recv(1024).decode('utf-8')
print(received_msg)
