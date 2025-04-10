import socket


HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"Connected to server {HOST}:{PORT}")

while True:
    
    client_message = input("You: ")
    client.send(client_message.encode())

    
    server_message = client.recv(1024).decode()
    if not server_message:
        break
    print(f"Server: {server_message}")

client.close()