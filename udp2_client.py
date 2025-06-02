import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

def receive_messages(sock):
    while True:
        data, _ = sock.recvfrom(1024)
        message = data.decode()
        print(f"\nServer: {message}")
        if message.lower() == "exit":
            break

def send_messages(sock, server_addr):
    while True:
        msg = input("Client: ")
        sock.sendto(msg.encode(), server_addr)
        if msg.lower() == "exit":
            break

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    server_addr = (SERVER_HOST, SERVER_PORT)
    s.sendto("Hello from client!".encode(), server_addr)

    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
    send_messages(s, server_addr)
