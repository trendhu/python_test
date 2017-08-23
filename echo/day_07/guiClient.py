import socket
from tkinter import *

class xx:
    def __init__(self):
        window = Tk()

        entry = Entry(window)
        entry.pack()
        button = Button(window, text = "发送", command = self.sendFn)
        button.pack()

        mainloop()



    def sendFn(self):
        if self.client =="":
            self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #给客户端套接字绑定IP和端口
            self.client.connect(("localhost", 8000))
            # 客户端给服务器发送数据
        mystring  = self.msg1.get()
        mystring = my1.encode()
        self.client.send(mystring)
        #接收服务端数据
        data = client.recv(1024)
        print("server：" + data.decode())
        self.entry["text"] = " "
        self.msg1.set(" ")



xx()