# echo-client.py

import socket
import pickle

def pickleTesting():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((HOST, PORT))
        data = s.recv(1024000)
        deSerialized = pickle.loads(data).run()
        
        s.sendall(deSerialized)
        print("done")


def helloWorld():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((HOST, PORT))
        data = s.recv(1024000)
        s.sendall(data)
        print("done")
        '''
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")
    '''

if __name__ == "__main__":
    pickleTesting()