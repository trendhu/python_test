from tkinter import * 
from wxpy import *


class WidgetsDemo:
    def __init__(self):
        
        self.bot = Bot(cache_path=True)
        # self.friendStart = StringVar()
        # self.fr = ""

        window = Tk()
        window.title("MyWeChat_v0.0.2")
        #添加一个多选按钮和单选按钮到frame1 
        frame1 = Frame(window)
        frame1.pack()#看下面的解释（包管理器） 

        self.userName = self.bot.self.name



        nameLabel = Label(frame1, text = "用户：" + self.userName)
        exitButton = Button(frame1, text = "退出", command=exit)
        nameLabel.grid(row = 1, column = 1)
        exitButton.grid(row = 1, column = 4)


        #-----------------查找好友-----------------
        frame2 = Frame(window)
        frame2.pack() 
        label1 = Label(frame2, text = "请输入名字") 
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name) 

        btGetName = Button(frame2, text = "查询", command = self.searchFriend) 

        self.label2 = Label(frame2, text = self.name.get(), fg='black')

        label1.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        self.label2.grid(row = 2, column = 1)




        #-----------------发送信息-----------------
        frame3 = Frame(window)
        frame3.pack()

        self.sing = StringVar()
        label4 = Label(frame3, text = "请输入信息")
        self.label3 = Label(frame3, text = "")
        entryName2 = Entry(frame3, textvariable = self.sing) 
        btGetName2 = Button(frame3, text = "发送", command = self.sendFriend)

        label4.grid(row = 1, column = 1)
        entryName2.grid(row = 1, column = 2)
        btGetName2.grid(row = 1, column = 3)
        self.label3.grid(row = 2, column = 1)




        #-----------------显示好友列表-----------------
        frame4 = Frame(window)
        frame4.pack()

        self.allFriends = self.bot.friends().search("", sex=MALE)
        

        text = Text(window)
        text.pack()

        for item in self.allFriends:
            print(item)
            print(item.nick_name)
            # text.insert(END, item.user_name)

        window.mainloop() 

    #查询好友是否存在    
    def searchFriend(self): 

        # print(self.name.get())
        friends = self.bot.friends().search(self.name.get(), sex=MALE)
        self.label2["text"] = self.name.get()
        if len(friends) > 0:
            if len(friends) == 0:
                # self.fr = "True"
                self.label2["fg"] = "green"
                # print("true")
            else:
                self.label2["fg"] = "black"
                self.label2["text"] = self.name.get() + ' 重复出现'
        else:
            # self.fr = "False"
            self.label2["fg"] = "red"
            # print("false")

    def sendFriend(self):
        self.bot.friends().search(self.name.get(), sex=MALE)[0].send(self.sing.get())
        self.label3["text"] = self.sing.get() + "发送成功"


        

WidgetsDemo()























