import os
import sys
import platform
#区分一下os、sys、platform三个模块：
# 
# os提供操作系统的接口，
# 常用的有文件系统相关和进程相关
# 例如：
# os.path.walk (遍历目录)
# os.getpid (获取进程id)
# 
# sys提供python解释器系统的通用配置和函数，
# 影响着解释器的行为注意这里的系统不是操作系统，
# 而是python解释器这个“系统”
# 例如：
# sys.version (python版本而非os版本)
# sys.path (模块搜索路径，不是os的环境变量)
# sys.getrecursionlimit (最大嵌套调用层数)
# sys.getrefcount (获取对象的引用计数)
# 
# platform提供平台相关的信息
# 例如：
# platform.architecture (操作系统和位数)
# platform.processor (处理器版本)

#os.name字符串指示你正在使用的平台。
# 比如对于Windows，它是'nt'，
# 而对于Linux/Unix用户，它是'posix'
print("当前所用的系统为 ----->  " + os.name)

#os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径
print("当前目录为：  ----->  " + os.getcwd())

#os.getenv()和os.putenv()函数分别用来读取和设置环境变量
print("JDK环境变量为  ----->  " + os.getenv("JAVA_HOME"))

#返回指定目录下的所有文件和目录名
a = os.listdir()    #返回值为 list(数组) 类型
print(a[0])

#使用os.sep可以取代操作系统特定的路径分割符
print(os.sep)

#os.linesep字符串给出当前平台使用的行终止符。
# 例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
print("sssssssssssssss" + "aaaaaaaaaaaaaa")
print("sssssssssssssss" + os.linesep + "aaaaaaaaaaaaaa")

#os.path.split()函数返回一个路径的目录名和文件名。
# 如：>>> os.path.split('/home/swaroop/byte/code/poem.txt')，
# 其结果为：('/home/swaroop/byte/code', 'poem.txt')
#此目录文件不必真实存在
print(os.path.split('/home/swaroop/byte/code/poem.txt'))

#os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
# 类似地，os.path.existe()函数用来检验给出的路径是否真地存在
print(os.path.isfile('G:/python/day_03/taobao/赵颖/运动装/0.jpg'))
print(os.path.isdir('G:/python/day_03/taobao/赵颖/运动装/0.jpg'))

#sys.argv: 可从命令行中获得参数。
# sys.argv[0]表示程序名，sys.argv[1]即为第一个参数
#返回结果为 list(数组) 类型
print("参数  --->  " + str(sys.argv))

#sys.platform：获得操作系统类型
#64位系统也为WIN32
#实际上这个`win32`应该是指Win32 API。
print(sys.platform)

#下面的结果为：AMD64
print(platform.machine())


#???????????????????????????????????????

#sys.exit(n)：执行至主程序的末尾时,解释器会自动退出.
#  但是如果需要中途退出程序, 你可以调用sys.exit 函数, 
# 它带有一个可选的整数参数返回给调用它的程序. 
# 这意味着你可以在主程序中捕获对sys.exit 的调用。
# （注：0是正常退出，其他为不正常，可抛异常事件供捕获!）
# def ee():
#     sys.exit()

# print(ee())

# print("dddddddddddddddddddddd")

#???????????????????????????????????????


#获取python版本而非os版本
print(sys.version)
