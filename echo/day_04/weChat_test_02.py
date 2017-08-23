
#搜索聊天对象
# 通过 .search() 获得的搜索结果 均为列表
# 若希望找到唯一结果，可使用 ensure_one()

from wxpy import *

bot = Bot(cache_path=True, console_qr=2)

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')


# 搜索名称包含 '吕小布' 的深圳男性好友
found = bot.friends(update=False).search('吕小布', sex=MALE)
print(found)
# [<Friend: 吕小布>]
# 确保搜索结果是唯一的，并取出唯一结果
huang = ensure_one(found)
print(huang)
# <Friend: 吕小布>


# 搜索名称包含 '66'，且成员中包含 `huang` 的群聊对象
wxpy_groups = bot.groups().search('66', [huang])
# [<Group: wxpy 交流群 1>, <Group: wxpy 交流群 2>]
print(wxpy_groups)

# 在刚刚找到的第一个群中搜索
group = wxpy_groups[0]
print(wxpy_groups[0])
# 搜索该群中所有浙江的群友
found = group.search(province='河南')
# [<Member: 浙江群友 1>, <Group: 浙江群友 2>, <Group: 浙江群友 3> ...]
print(found)

# 搜索名称含有 'wxpy' 的任何聊天对象
found_2 = bot.search('张')
print(found_2)
# [<Friend: wxpy 机器人>, <Group: wxpy 交流群 1>, <Group: wxpy 交流群 2>]







# 进入 Python 命令行、让程序保持运行
embed()













