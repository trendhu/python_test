import socket

#此行定义了三个变量
serverAddress = (HOST, PORT) = "", 8000

#创建套接字
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#选项
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#给套接字绑定 IP地址 和 端口号
serverSocket.bind(serverAddress)

#服务器开始监听(设置一次允许的访问数量)
serverSocket.listen(10)

print("Server is running on post", PORT)

while True:
    #接受客户端请求
    client, clientAddress = serverSocket.accept()

    #接收客户端发送数据(括号内参数为 一次接收的数据大小)
    request = client.recv(1024)

    
    print("client:  ", request.decode())

    #给客户端发送数据
    # client.send("hello")


    response = b"""\
    HTTP/1.1 200 ok

    hello world
        """;

    client.sendall(response)

    #关闭和服务器的连接
    # client.close()




