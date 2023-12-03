# echo-server.py

import socket
import pickle
from abc import ABC, abstractmethod

helloExec = """
response = "hello world"
"""


def execMainTesting():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        data = bytes(helloExec, 'utf-8')

        conn, addr = s.accept()
        with conn:
            conn.sendall(data)    
            print(f"Connected by {addr}")
            while True:
                recieved = conn.recv(1024000)
                if not recieved:
                    break
                print(f"Received {recieved!r}")

def helloWorldTesting():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        data = b"Hello World"
        conn, addr = s.accept()
        with conn:
            conn.sendall(data)    
            print(f"Connected by {addr}")
            while True:
                recieved = conn.recv(1024)
                if not recieved:
                    break
                print(f"Received {recieved!r}")


if __name__ == "__main__":
    execMainTesting()