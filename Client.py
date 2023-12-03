# echo-client.py

import socket

responseDict = {}

def execTesting():
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024000)
        data = data.decode("utf-8")
        exec(data, responseDict)
        s.sendall(bytes(responseDict['response'], 'utf-8'))
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
    execTesting()