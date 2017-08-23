

print("----------日期和时间----------")

import time;
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)


# 获取当前时间
# # 从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
localtime = time.localtime(time.time())
print ("Local current time :", localtime)


# 获取格式化的时间
# 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print ("Local current time :", localtime)


# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar
cal = calendar.month(2008, 1)   #打印出 2008 年 1 月的日历
print ("Here is the calendar:" , cal);










