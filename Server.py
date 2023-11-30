# echo-server.py

import socket
import pickle
from abc import ABC, abstractmethod

#PICKLE CLASS
class command(ABC):
    @abstractmethod
    def run(self):
        pass

class helloPickle(command):
    # Hellow world pickle
    def run(self):
        created_pickle = pickle.dumps("Hello pickle!")
        return created_pickle
    
def pickleMainTesting():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    to_send = pickle.dumps(helloPickle())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        data = pickle.dumps(helloPickle())

        conn, addr = s.accept()
        with conn:
            conn.sendall(data)    
            print(f"Connected by {addr}")
            while True:
                recieved = conn.recv(1024000)
                deSerialized = pickle.loads(recieved)
                if not recieved:
                    break
                print("Received", deSerialized)

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
    pickleMainTesting()