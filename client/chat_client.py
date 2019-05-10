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
    
    try:
        while True:
            # Recv incoming msgs
            usernameHeader = clientSocket.recv(HEADER_LENGTH)
            if not len(usernameHeader):
                print("[-] Server closed -> Disconnecting...")
                sys.exit()
            
            usernameLength = int(usernameHeader.decode('utf-8').strip())
            username = clientSocket.recv(usernameLength).decode('utf-8')

            message_header = clientSocket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = clientSocket.recv(message_length).decode('utf-8')

            print(f"{username}: {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('[!] Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print("[!] General Error", str(e))
        sys.exit()