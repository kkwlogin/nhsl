import socket

# Server Configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports > 1023)

# Create socket object with IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from client: {data.decode()}")
            conn.sendall(data)  # Echo the data back
