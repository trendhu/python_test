import tool
import urllib.request
import ssl
import re
import os
import json

class Spider:

    def __init__(self):
        self.homeUrl = "https://mm.taobao.com/json/request_top_list.htm"
        self.tool = tool.Tool() #正则表达式(匹配字符串)

    def savePagesInfo(self, pageIndex):
        urlString = self.homeUrl + "?page=" + str(pageIndex)
        response = urllib.request.urlopen(urlString)
        pageString = response.read().decode('gbk')
        # print(pageString)

        #正则表达式
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        
        itemArr = re.findall(pattern, pageString)
        #(查找规则, 查找对象, 设置)

        # print(itemArr)

        contents =[]
        for item in itemArr:
            # print(item[2])
            contents.append([item[0], item[1], item[2], item[3], item[4]])
        
        for item in contents:
            mm_name = item[2]
            # print("模特叫做：" + item[2], "年龄：" + item[3], "家庭地址：" + item[4], "个人信息：" + item[0])
            mm_url = item[0]
            pattern = re.compile(r'\d+') 
            mm_id = pattern.findall(mm_url)[0]  #通过 pattern.findall() 方法得到的数据，返回结果是list(数组)类型
            # print(pattern.findall(mm_url))
            # print(mm_id)

            albumsUrl = "https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=" + mm_id
            albumReponse = urllib.request.urlopen(albumsUrl)
            albumReponseString = albumReponse.read().decode('gbk')
            # print(albumReponseString)

            resString = r"<h4>(.*?)</h4>"
            #  r 代表正则表达式
            #  空格内的 .*?  表示你要拿取的内容
            mmAlbums = re.findall(resString, albumReponseString, re.I|re.S|re.M)
            # print(mmAlbums)

            for item in mmAlbums:
                #相册的名字
                res = r"<a .*?>(.*?)</a>"
                albumName = re.findall(res, item, re.S|re.I|re.M)
                # print(albumName[0].strip())
                albumName = albumName[0].strip()
                # print(mm_name + "  ---->  " + albumName)

                #相册的ID
                #获取相册的地址
                # print(item)
                resForId = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
                mm_link = re.findall(resForId, item, re.I|re.M|re.S)[0]
                print(mm_link)
                
                #根据人和相册的名字去创建文件夹
                albumName = albumName.replace("...", "")
                albumPath = "taobao_1/" + mm_name + "/" + albumName
                albumPath = albumPath.strip()

                isExist = os.path.exists(albumPath)
                if not isExist:
                    os.makedirs(albumPath)
                else:
                    print(albumPath + "  --->  已存在")


                #很多相册的地址
                mm_link = "http:" + mm_link

                # mm_link_result = urllib.request.urlopen(mm_link)

                #url 解析
                result = urllib.parse.urlparse(mm_link)
                parms  = urllib.parse.parse_qs(result.query, True)

                pageNumber = 1

                #某个相册的地址
                mm_link = "https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=" + parms["user_id"][0] + "&album_id=" + parms["album_id"][0] + "&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2F687471686%2FTB1jlwCHXXXXXcvXXXXXXXXXXXX_!!687471686-0-tstar.jpg&page=" + str(pageNumber) + "&_ksTS=1502652171209_154&callback=jsonp15"
                images = urllib.request.urlopen(mm_link)
                imagesString = images.read().decode('gbk')
                # print(imagesString)

                imagesJson = json.loads(imagesString.strip()[9:-1])
                imagesList = imagesJson["picList"]

                for index, oneImage in enumerate(imagesList):
                    imagePath = albumPath + "/" + str(index) + ".jpg"
                    if os.path.exists(imagePath):
                        # print(albumPath + "/" + str(index) + ".jpg   已存在")
                        continue

                    oneImageUrl = "http:" + oneImage["picUrl"]
                    print("正在保存：" + imagePath)
                    f = open(imagePath, "wb")
                    oneImageData = urllib.request.urlopen(oneImageUrl).read()
                    f.write(oneImageData)
                    f.flush()
                    f.close()






spider = Spider()

spider.savePagesInfo(2)
















