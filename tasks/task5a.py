import socket

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server started on {HOST}:{PORT}... Waiting for connection...")

client_socket, client_address = server.accept()
print(f"Connected with {client_address}")

while True:
    
    client_message = client_socket.recv(1024).decode()
    if not client_message:
        break
    print(f"Client: {client_message}")

    
    server_message = input("You: ")
    client_socket.send(server_message.encode())

client_socket.close()
server.close()