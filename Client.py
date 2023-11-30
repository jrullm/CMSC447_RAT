# echo-client.py
# https://realpython.com/python-sockets/#tcp-sockets

import socket
import pickle
import sys

MAX_SIZE = sys.maxsize

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
to_send

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        
        with conn:
            #Receiving data from client
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(MAX_SIZE)
                if not data:
                    break
                to_send = pickle.loads(data).run()
                
            # Sending data to client
            s.connect((HOST, PORT))
            s.sendall(to_send)
