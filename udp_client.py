import socket

# Server Configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port used by the server

# Create UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        s.sendto(message.encode(), (HOST, PORT))
        data, server = s.recvfrom(1024)
        print(f"Received from server: {data.decode()}")
