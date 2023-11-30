#Here is the Server by Colby and Co.
# https://realpython.com/python-sockets/#tcp-sockets

# echo-server.py

import socket
import pickle
import sys

from abc import ABC, abstractmethod

MAX_SIZE = sys.maxsize

class command(ABC):
    @abstractmethod
    # Pickle object
    created_pickle
    
    def run(self):
        pass

class helloPickle(command):
    # Hellow world pickle
    def run(self):
        created_pickle = pickle.dumps("Hello pickle!")
        return created_pickle

if __name__ == "__main__":

    to_send = pickle.dumps(helloPickle())
    
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(MAX_SIZE)
                if not data:
                    break
                conn.sendall(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(to_send)
        data = s.recv(MAX_SIZE)
