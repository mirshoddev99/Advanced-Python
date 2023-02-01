import socket
import threading


nickname = input("Enter a nickname: ")

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        msg = f"{nickname}: {input('')}"
        client.send(msg.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
