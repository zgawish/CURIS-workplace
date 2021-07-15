import socket

HEADER = 1024
PORT = 5050
SERVER = "10.128.0.3" # IP of head node
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
REQUEST_MSG = "!REQUEST"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
msg = input()
send(msg)
msg = input()
send(msg)
input()
send(REQUEST_MSG)
input()
send(DISCONNECT_MSG)
