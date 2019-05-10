import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = input("[*] Enter server ip: ")
PORT = int(input("[*] Enter server port: ")) 
USERNAME = input("[*] Enter your username: ")
print("[*] Type '/exit' to exit server")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))
clientSocket.setblocking(False)

username = USERNAME.encode('utf-8')
usernameHeader = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
clientSocket.send(usernameHeader+username)

while True:
    message = input(f"{USERNAME}> ")

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode('utf-8')
        clientSocket.send(message_header+message)