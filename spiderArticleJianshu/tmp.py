# coding:utf-8
from bs4 import BeautifulSoup

soup = BeautifulSoup('<div>早上9点了</div>你好世界<div>世界和平</div>','lxml')
info = [s.extract() for s in soup('div')]
print(info)
print(soup.text)