import socket
import select
import errno

HEADER_LENGTH = 10

IP = input("[*] Enter server ip: ")
PORT = int(input("[*] Enter server port: ")) 
USERNAME = input("[*] Enter your username: ")
