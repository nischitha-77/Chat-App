import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            client_socket.close()
            break

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Username input
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Sending messages
while True:
    message = input()
    if message.lower() == '/exit':
        client.send('/exit'.encode('utf-8'))
        print("You left the chat.")
        client.close()
        break
    client.send(message.encode('utf-8'))
