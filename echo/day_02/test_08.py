from urllib import request # 请求url, 支持 HTTP(0.9/1.0) / FTP / 本地文件 / URL
from urllib import parse # 解析url, 支持 file / ftp / gopher / hdl / http / https / imap / mailto / mms / news / nntp / prospero / rsync / rtsp / rtspu / sftp / shttp / sip / sips / snews / svn / svn+ssh / telnet / wais
from urllib import robotparser # 分析 robots.txt 文件
from urllib import error # 异常
import re # 正则模块
import os
 
 
 
# os.mkdir("images")
# -- 获取网页源代码 --
f = request.urlopen("https://www.douyu.com")
data = f.read().decode("utf-8")

# -- 获取网页源码中的图片地址 --
# 方式一: 正则的方式
images = re.findall(r'data-original="(.*?\.(jpg|png))"', data)
print(images[0])