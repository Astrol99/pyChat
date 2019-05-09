import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 6969

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOCK_SEQPACKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen(5)

socket_list = [server_socket]
