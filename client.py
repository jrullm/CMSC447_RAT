# echo-client.py

import socket
import pickle
import subprocess

def pickleTesting():
    newValue = None
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024000)
        deSerialized = pickle.loads(data)
        exec(deSerialized)

        reSerialized = pickle.dumps(newValue)
        s.sendall(reSerialized)
        print("done")

__name__ = "__main__"

if __name__ == "__main__":
    pickleTesting()