import urllib.request
import ssl

context = ssl._create_unverified_context

write_test = "这是一段测试数据信息"
f = open("test_01.txt", "w", encoding="utf-8")
f.write(write_test)
# read_test = f.readlines()
# print(read_test)
f.flush()
f.close()