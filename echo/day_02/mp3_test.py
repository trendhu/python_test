import urllib.request
import ssl

context = ssl._create_unverified_context()

def saveMp3(url, index):
    mp3Data = urllib.request.urlopen(url, context=context).read()
    print("正在保存第" + str(index) + "个音乐")
    f = open("G:/python/day_02/mp3_test/mp3_" + str(index) + ".mp3" , "wb")
    f.write(mp3Data)
    f.flush()
    f.close()

mp3s = ["http://m10.music.126.net/20170813120954/f704b82a979c04bc9702785b8bc1f443/ymusic/7396/3770/aea3/2231f41a9bbea90cfe5f735a9ba750b2.mp3", "http://m10.music.126.net/20170813121037/a3a2adb91ae98354a13f91527f9833cc/ymusic/7396/3770/aea3/2231f41a9bbea90cfe5f735a9ba750b2.mp3", "http://m10.music.126.net/20170813121107/6a7e9c3fe85483fc55b4ca694da0e865/ymusic/7396/3770/aea3/2231f41a9bbea90cfe5f735a9ba750b2.mp3"]

for index , mp3 in enumerate(mp3s):
    saveMp3(mp3 , index)