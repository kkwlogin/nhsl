import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode()
        print(f"\nClient ({addr}): {message}")
        if message.lower() == "exit":
            break

def send_messages(sock, client_addr):
    while True:
        msg = input("Server: ")
        sock.sendto(msg.encode(), client_addr)
        if msg.lower() == "exit":
            break

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("UDP Server is ready and waiting for messages...")

    data, client_addr = s.recvfrom(1024)
    print(f"Connected to client: {client_addr}")
    print(f"Client: {data.decode()}")

    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
    send_messages(s, client_addr)
