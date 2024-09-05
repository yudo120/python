import socket

# Initialize Socket Instance
sock = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 5555
host = '25.37.63.151'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')

# Send a greeting to the server
sock.send('A message from the client'.encode())

# Receive the filename from the server
filename = sock.recv(1024).decode()

# Write File in binary
with open(filename, 'wb') as file:
    # Keep receiving data from the server
    line = sock.recv(1024)
    while line:
        file.write(line)
        line = sock.recv(1024)

print('File has been received successfully.')

sock.close()
print('Connection Closed.')
