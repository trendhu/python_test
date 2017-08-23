
from tkinter import *

class ChangeLableq:
    def __init__(self):
        #创建一个主窗口
        root = Tk()

        #创建一个标签
        label = Label(root, text="wdnnda,smdsam,", fg="red")

        #将标签加入到主窗口中
        label.pack()

        button = Button(root, text="aaa", command=self.sendFunction)
        button.pack()
        
        #让程序在主线程里启动一个环路进程
        mainloop()

    def sendFunction(self):
            print("ssssssssssssssss")


ChangeLableq()













