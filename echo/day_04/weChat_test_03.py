

#加好友和建群

from wxpy import *

bot = Bot(cache_path=True, console_qr=2)

# bot.add_friend('hjzzao', "hhhhhhhh")
userName = bot.self.name
# print(userName)
# print(type(userName))


print(len(bot.friends().search("吕小布", sex=MALE)))

















