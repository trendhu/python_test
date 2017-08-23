import urllib.request;
url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png';
page = urllib.request.urlopen(url);
# print(page);
data  = page.read();
# print(data);
# print(type(data));
f = open("tupian.png","wb");

f.write(data);
f.flush();
f.close();
