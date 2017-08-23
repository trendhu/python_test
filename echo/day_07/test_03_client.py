import socket

#创建客户端套接字
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#给客户端套接字绑定IP和端口
client.connect(("192.168.7.116", 8888))

# 客户端给服务器发送数据
client.send(b"hadoop")

#接收服务端数据
while True:
    data = client.recv(1024)
    print("server：" + data.decode())












