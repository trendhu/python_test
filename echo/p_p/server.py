import socket
from tkinter import *

serverAddress = (HOST, PORT) = "",8810

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

serverSocket.bind(serverAddress)

serverSocket.listen(10)

print("Server is running on post", PORT)

while True:
    clientin, clientAddress = serverSocket.accept()
    request = clientin.recv(1024).decode()
    outIp = request.split(";")[0]
    outString = request.split(";")[1]
    clientout = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientout.connect((outIp, 8000))
    clientout.send(outString)
    





