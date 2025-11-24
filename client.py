import socket

# REPLACE THIS WITH VM1's REAL IP ADDRESS
SERVER_IP = '34.131.165.237' 
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

print(f"Connected to server {SERVER_IP}:{PORT}")

try:
    while True:
        # Send message
        msg = input("You: ")
        client_socket.sendall(msg.encode())

        # Receive response
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")
finally:
    client_socket.close()