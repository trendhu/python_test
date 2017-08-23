from wxpy import *

bot = Bot(cache_path=True)


#添加好友功能未成功，并不知道要添加陌生人如何添加
# 添加用户为好友
# Bot.add_friend(user, verify_content='')
# 参数:	
#     user – 用户对象，或 user_name
#     verify_content – 验证说明信息





# 添加/关注 公众号
# Bot.add_mp(user)
# 参数:	user – 公众号对象，或 user_name

# bot.add_mp('老郭单口')


# 接受用户为好友
# Bot.accept_friend(user, verify_content='')
# 参数: 
# user – 用户对象或 user_name
# verify_content – 验证说明信息
# 返回:	新的好友对象


# ----------自动接受好友请求----------
# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if 'wxpy' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，我自动接受了你的好友请求')




