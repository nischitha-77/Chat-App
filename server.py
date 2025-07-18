import socket
import threading
import datetime

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

clients = []
usernames = {}

def handle_client(client_socket):
    username = client_socket.recv(1024).decode('utf-8')
    usernames[client_socket] = username
    broadcast(f"{username} has joined the chat.", client_socket)
    print(f"{username} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message == '/exit':
                break

            timestamp = datetime.datetime.now().strftime('%H:%M:%S')
            full_message = f"[{timestamp}] {username}: {message}"
            print(full_message)
            broadcast(full_message, client_socket)

        except:
            break

    # Client disconnected
    clients.remove(client_socket)
    broadcast(f"{username} has left the chat.", client_socket)
    print(f"{username} disconnected.")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode('utf-8'))

# Main server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server running on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
