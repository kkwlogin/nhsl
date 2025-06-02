import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 65432

def handle_receive(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        sys.stdout.write(f"\nClient: {data.decode()}\nServer: ")
        sys.stdout.flush()

def handle_send(conn):
    while True:
        msg = input("Server: ")
        conn.sendall(msg.encode())
        if msg.lower() == "exit":
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is listening...")
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
    handle_send(conn)
