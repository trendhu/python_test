from wxpy import *
bot = Bot()
# 获取好友
dear = bot.friends().search('四大爷')[0]
#  注册获得个人的图灵机器人key 填入
tuling = Tuling(api_key='c9aca7459f894fd39dded7c3ca6d6719')
# 使用图灵机器人自动与指定好友聊天
@bot.register(dear)
def reply_my_friend(msg):    
    print(msg)
    tuling.do_reply(msg)

embed()