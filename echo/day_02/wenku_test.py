import json
import urllib.request
import ssl
import os

context = ssl._create_unverified_context()

path = "G:/python/day_02/ppt_test/"

urlStr = "https://wenku.baidu.com/browse/getbcsurl?doc_id=7f25793443323968011c92dc&pn=1&rn=99999&type=ppt&callback=jQuery11010889315656298626_1502606956441&_=1502606956443"

response = urllib.request.urlopen(urlStr)   #获取一个网络连接

inputStr = response.read().decode() #对读取结果进行解码

inputStrArr_1 = inputStr.split("(") #对字符串进行分割

inputStrArr_2 = inputStrArr_1[1].split(")")

jsonStr = inputStrArr_2[0]

jsonData = json.loads(jsonStr)

listAll = jsonData["list"]

# print(response.read().decode())

# print(listAll)


def saveImage(url, index, path):
    imageData = urllib.request.urlopen(url, context=context).read()
    print("正在保存第" + str(index) + "个图片")
    f = open(path + "ppt_" + str(index) + ".jpg" , "wb")
    f.write(imageData)
    f.flush()
    f.close()

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print("文件夹创建成功")
    else:
        print("文件已存在")

mkdir(path)

for item in listAll:
    # print(item)
    # print(item["page"])
    # print(item["zoom"])
    page = item["page"]
    pageUrl = item["zoom"]
    saveImage(pageUrl , page, path)












