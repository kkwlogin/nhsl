import socket

# Server Configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port used by the server

# Create socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server.")
    
    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Received from server: {data.decode()}")
