import socket

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports > 1023)

# Create UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Server listening on {HOST}:{PORT}...")
    
    while True:
        data, addr = s.recvfrom(1024)  # buffer size is 1024 bytes
        print(f"Received message: {data.decode()} from {addr}")
        s.sendto(data, addr)  # Echo the data back to the client
