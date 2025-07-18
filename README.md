# Python Multi-Client Chat Application

This is a simple terminal-based chat application developed in Python using TCP sockets and multi-threading. It allows multiple clients to communicate with each other in real-time through a centralized server.

Features:
- Supports multiple clients simultaneously using threading
- Real-time message broadcasting to all connected clients
- Unique usernames for each client
- Timestamps attached to every message
- Join and leave notifications for users
- '/exit' command allows clients to disconnect gracefully

Project Structure:
- server.py : Handles client connections, broadcasts messages, and manages server-side communication.
- client.py : Connects to the server, sends messages, and receives messages from other clients via the server.
- README.md : Project documentation.

How to Run:

1. Clone the repository or download the project files.

2. Start the server by running:
   python server.py

   The server will start and listen on 127.0.0.1 at port 12345.

3. In separate terminal windows or systems, start one or more clients by running:
   python client.py

4. When prompted, enter your username to join the chat.

5. Start typing messages to chat with all connected users.

6. To exit the chat, type '/exit' in the client terminal.

Technologies Used:
- Python 
- Socket programming using TCP
- Multi-threading for handling concurrent clients
- Basic terminal input/output



