import requests
from bs4 import BeautifulSoup
import pymysql

url = 'https://www.jianshu.com/p/5a6d780fd8cd'

headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
response = requests.get(url,headers=headers)

html = response.content
html = html.decode('utf8')
soup = BeautifulSoup(html, 'lxml')



# 删除标签
for item in soup.find_all(["svg","header","footer","aside"]):
    item.decompose()

for item in soup.find_all('script',attrs={"type":"application/json"}):
    item.decompose()


div = soup.find_all(id="__next")
ddvi = div[0].children
res = [item for item in ddvi]
res1 = res[1:]
for item in res1:
    item.decompose()

tmp = div = soup.find_all('div',attrs={"class":"_gp-ck"})
tmp = tmp[0].children
tmplist = [item for item in tmp]
tmplist1 = tmplist[1:]
for item in tmplist1:
    item.decompose()


# img 标签 需要获取到 data-original-src 的值，然后在拼接http，再在img里面添加 src属性
imgIterator = soup.find_all('img')
for item in imgIterator:
    pictureUrl = "http:"+item["data-original-src"]
    item['src'] = pictureUrl


tag = soup.h1
title = tag.string
print(tag.string)
body = str(soup)
body = body.replace("'",'"')
print(body)

# conn = pymysql.Connect(user="root",password='123456',host='127.0.0.1',database='simblog')
# curses = conn.cursor()
#
# sql = "insert into topics(title,body) value('{title}','{body}')".format(title=title,body=body)
# curses.execute(sql)
# conn.commit()
#
# curses.close()
# conn.close()

with open('demo1.html','wb') as fp:
    fp.write(body.encode('utf8'))