import urllib.request
import ssl

context = ssl._create_unverified_context()

def saveImage(url, index):
    imageData = urllib.request.urlopen(url, context=context).read()
    print("正在保存第" + str(index) + "个图片")
    f = open("G:/python/day_02/image_test/image_" + str(index) + ".jpg" , "wb")
    f.write(imageData)
    f.flush()
    f.close()

images = ["https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502604679340&di=6879d412a2669772c37253e2eef902fc&imgtype=0&src=http%3A%2F%2Fimg5q.duitang.com%2Fuploads%2Fitem%2F201210%2F03%2F20121003143941_VXNLS.thumb.700_0.jpeg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502604679340&di=fd064d634737775e78235caa3be73af1&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201510%2F25%2F20151025131445_dK8MH.jpeg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502604679340&di=ee21f641d2832c20617ebd67caaed4fe&imgtype=0&src=http%3A%2F%2Ff8.topitme.com%2F8%2F14%2Fa7%2F1159708876983a7148o.jpg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502604679339&di=f58e0ec8bc20be97759cc8fd7e729651&imgtype=0&src=http%3A%2F%2Fv1.qzone.cc%2Fskin%2F201411%2F15%2F17%2F33%2F54671e027790a109.jpg%2521600x600.jpg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502604679339&di=e41023a667cc4c8f0fb6d2df26affe07&imgtype=0&src=http%3A%2F%2Fimg4.duitang.com%2Fuploads%2Fitem%2F201406%2F10%2F20140610144149_E3FrP.thumb.600_0.jpeg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1502604679339&di=a361f005ce3168cb3dd4a44001587ec6&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201507%2F14%2F20150714155243_sN5vG.jpeg",]

for index , image in enumerate(images):
    saveImage(image , index)
