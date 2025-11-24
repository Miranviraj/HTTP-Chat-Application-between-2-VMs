import socket

HOST = ""  # Empty string means listen on all interfaces
PORT = 5000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        # Receive message
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        # Send response
        msg = input("You: ")
        conn.sendall(msg.encode())
finally:
    conn.close()