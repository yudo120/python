import socket
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Initialize Socket Instance
sock = socket.socket()
print("Socket created successfully.")

# Defining port and host
port = 5555
host = '25.37.63.151'

# Binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Get data from the client
    data = con.recv(1024)
    print(data.decode())

    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(title="Selecciona un archivo",
                                           filetypes=[("Todos los archivos", "*.*")])

    # Send the filename first
    filename = file_path.split('/')[-1]  # Extract the file name from the path
    con.send(filename.encode())

    # Send the file content
    with open(file_path, 'rb') as file:
        line = file.read(1024)
        while line:
            con.send(line)
            line = file.read(1024)

    print('File has been transferred successfully.')

    con.close()
