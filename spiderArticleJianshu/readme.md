只要可以把整个网页获取下来，然后删除掉不必要的div，和js逻辑，那么就可以达到保存一个文章的目的了

request 获取到的响应似乎无法获取源代码的js
> 这里其实也是可以的，我用pycharm 打开一个服务似乎就无法识别样式，但是直接本地打开就有样式了

因此转到 selenium 测试，教程：https://zhuanlan.zhihu.com/p/111859925

chrome驱动 https://sites.google.com/corp/chromium.org/driver/
> 这里安装驱动的时候需要保证本地`driver`的版本和chrome的大版本保持一致
> chrome 新开一个tab页，输入`chrome://version/`,页面输出
`Google Chrome	100.0.4896.127 (正式版本) （64 位） (cohort: 100_Win_127) `
> 
> 这里的第一个100就是大版本号

提示错误信息`DeprecationWarning: executable_path has been deprecated, please pass in a Service object`
,[搜索后](https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python) 
发现只需要添加一个key：executable_path即可



需要以下几个知识点
 - 获取一个div下的所有的标签，最好返回的是一个list
 - 删除某个标签

### [BeautifulSoup基础操作](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/index.html)
#### new 一个 对象
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, features="html.parser")

```

#### 查找
```python

# 根据标签查找
imgs = soup.find_all("img")
# 根据属性查找
imgs = soup.find_all("img", attrs={"class": "avatar"})
# 根据样式查找（支持正则）
tabs = soup.find_all(style=re.compile(r'.*display:none.*?'))

```

#### 删除标签
```python
# 删除style中包含隐藏的标签
for i in self.soup.find_all(style=re.compile(r'.*display:none.*?')):
    i.decompose()

```

#### 获取标签属性
```python
# 获取img标签的src属性
imgs = soup.find_all('img')
for img in imgs:
    url = img.get("src")
    print(url)

```

#### 获取标签内文本
```python
# 获取文本（分隔符、去除空白）
soup.get_text(separator=" ", strip=True)

```

#### 根据css选择器选择标签
```python
 #获取a标签中具有href属性的标签
soup.select('a[href]')

```

#### 正则匹配标签
```python
# 选取所有的h标签，替换内容（去除h标签内的标签，只保留文本）
for i in soup.find_all(re.compile("^h[1-6]")):
	i.string = i.get_text()

```

#### 去除空标签
```python
# 删除空白标签（例如<p></p>、<p><br></p>, img、video、hr除外）
soup = BeautifulSoup(clean_content, features="html.parser")
for i in soup.find_all(lambda tag: len(tag.get_text()) == 0 and tag.name not in ["img", "video", "br"] and tag.name != "br"):
    for j in i.descendants:
        if j.name in ["img", "video", "br"]:
            break
    else:
        i.decompose()

```