from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="./chromedriver.exe")    # Chrome浏览器

url = 'https://www.jianshu.com/p/1531e12f8852'

# 打开网页
driver.get(url) # 打开url网页 比如 driver.get("http://www.baidu.com")

pagesource = driver.page_source
print(type(pagesource))
# headers = {
#     "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
# }

# with open('demo1.html','w',encoding='utf8') as fp:
#     fp.write(pagesource)

# 接下来就是识别html，剪切html BeautifulSoup
