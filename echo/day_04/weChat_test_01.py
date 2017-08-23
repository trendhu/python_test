# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True, console_qr=2)

# 机器人账号自身
#结果：<User: 无忧～『何愁』>
myself = bot.self
print(myself)
# myself 的数据类型：<class 'wxpy.api.chats.user.User'>
print(type(myself))

# 向文件传输助手发送消息
bot.file_helper.send('Hello from wxpy!')


# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('吕小布', sex=MALE)[0]

# 发送文本给好友
# my_friend.send('Hello WeChat!')
# 发送图片
# my_friend.send_image('3.jpg')

# 进入 Python 命令行、让程序保持运行


# 打印来自其他好友、群聊和公众号的消息
# @bot.register()
# def print_others(msg):
#     print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)

# # 自动接受新的好友请求
# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     # 接受好友请求
#     new_friend = msg.card.accept()
#     # 向新的好友发送消息
#     new_friend.send('哈哈，我自动接受了你的好友请求'




# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')

# 指定一个好友
# my_friend = bot.friends().search('游否')[0]

# 查看他的 puid
print(my_friend.puid)

#为 True 时，将自动消除手机端的新消息小红点提醒 (默认为 False)
Bot.auto_mark_as_read = False


# 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

# 发送消息给自己
bot.self.send('能收到吗？')

#获取所有好友
#Bot.friends(update=False)  参数:	update – 是否更新
#在
# friends = bot.friends()
# print(friends)


#获取所有群聊对象
#Bot.groups(update=False, contact_only=False)
# 一些不活跃的群可能无法被获取到，
# 可通过在群内发言，或修改群名称的方式来激活
# 参数:	
# update – 是否更新
# contact_only – 是否限于保存为联系人的群聊
#结果：[<Group: 无忧～『何愁』,平淡的幸福,胡亚杰>, <Group: 6666>, <Group: 16日本語の勉強>, <Group: 高三六班>]
# groups = bot.groups()
# print(groups)


#获取所有公众号
#Bot.mps(update=False)
#参数:	update – 是否更新
# mps = bot.mps()
# print(mps)


# 获取所有聊天对象
#Bot.chats(update=False)
#参数:	update – 是否更新
chats = bot.chats()
print(chats)



# 进入 Python 命令行、让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()







