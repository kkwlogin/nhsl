import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 65432

def handle_receive(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sys.stdout.write(f"\nServer: {data.decode()}\nClient: ")
        sys.stdout.flush()

def handle_send(sock):
    while True:
        msg = input("Client: ")
        sock.sendall(msg.encode())
        if msg.lower() == "exit":
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server.")
    threading.Thread(target=handle_receive, args=(s,), daemon=True).start()
    handle_send(s)
