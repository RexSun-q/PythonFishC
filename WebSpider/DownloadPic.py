import urllib.request
import os

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1592828621197&di=050415a49d45379067dfca59579eed8f&imgtype=0&src=http%3A%2F%2Fimg.qq-gg.net%2FUploads%2F2018-11-14%2F5beb9785f0ecd.jpg'
'''
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'

req = urllib.request.Request(url)
req.add_header('User-Agent',agent)
'''
response = urllib.request.urlopen(url)
read_img = response.read()

with open('/Users/sunzhiqi/PythonFishC/WebSpider/new.jpg','wb') as f:
    f.write(read_img)
