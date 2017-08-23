
from wxpy import *
import threading

bot = Bot(cache_path=True)

s = 0

def fun_timer():
    # s += 1
    my_friend = bot.friends().search('四大爷')[0]
    print(s)
    # 发送文本给好友
    my_friend.send('这是程序轰炸，请规避！！！')
    global timer
    timer = threading.Timer(3, fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()