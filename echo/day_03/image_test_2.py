from urllib import request
import ssl

context = ssl._create_unverified_context()

url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png'

imagePage = request.urlopen(url, context=context)

imageData = imagePage.read()

f = open('tt.png', 'wb')

f.write(imageData)

f.flush()

f.close()

















