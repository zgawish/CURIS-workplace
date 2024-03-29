import socket
import time

HEADER = 1024
PORT = 5050
SERVER = "10.128.0.3" # internal IP of head node
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
REQUEST_MSG = "!REQUEST"

start = time.time()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
end = time.time()
print("Time elapsed: " + str(end - start))


def send(msg):
    start = time.time()
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    end = time.time()
    print("Time elapsed: " + str(end - start))


msg = input("Input: ")
while msg != "": #cmd to run a command
    send(msg)
    msg = input("Input: ")
send(DISCONNECT_MSG)
