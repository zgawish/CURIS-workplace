import socket
import time

HEADER = 1024
PORT = 5050
SERVER = "10.128.0.3" # internal IP of head node
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
REQUEST_MSG = "!REQUEST"


def send(client, msg):
    start = time.time()
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    r_msg = client.recv(2048).decode(FORMAT)
    end = time.time()
    print("Time to Send and Recieve Message: " + str(end - start))
    return r_msg

def connect_client():
    start = time.time()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    end = time.time()
    print("Time to Connect: " + str(end - start))
    return client

def run_test():
    t_end = time.time() + (60 * 60 * 4)
    while time.time() < t_end:
        r_msg = send('Hello ' + str())
        if r_msg == "Message recieved":
            r_msg = send(DISCONNECT_MSG)
            print(r_msg)
        time.sleep(5)

run_test()