from wxpy import*

bot = Bot(cache_path=True)


# 通过机器人对象 Bot 的 chats(), friends()，groups(), mps() 方法, 
# 可分别获取到当前机器人的 所有聊天对象、好友、群聊，以及公众号列表。

# 而获得到的聊天对象合集 Chats 和 Groups 具有一些合集方法
# ，例如：Chats.search() 可用于按条件搜索聊天对象:

my_friend = bot.friends().search('游否', sex=MALE, city='深圳')[0]
# <Friend: 游否>


# 在找到好友(或其他聊天对象)后，
# 还可使用该聊天对象的 send 系列方法，对其发送消息

# 发送文本
my_friend.send('Hello, WeChat!')
# 发送图片
my_friend.send_image('my_picture.png')
# 发送视频
my_friend.send_video('my_video.mov')
# 发送文件
my_friend.send_file('my_file.zip')
# 以动态的方式发送图片
my_friend.send('@img@my_picture.png')


















