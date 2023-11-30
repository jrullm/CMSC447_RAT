# echo-client.py
# https://realpython.com/python-sockets/#tcp-sockets

import socket
import pickle
import sys

MAX_SIZE = sys.maxsize

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(MAX_SIZE)

print(f"Received {data!r}")#This is the client file By: Colby and Co.
