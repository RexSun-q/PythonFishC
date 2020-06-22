import urllib.request
import urllib.parse
import json

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
header = {}

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
header['User-Agent'] = agent

i = input('Enter Chinese:')

data['i'] = str(i)
data['from'] =  'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15928053157929'
data['sign'] = 'fd3bf0aa639d5322534d9220531d4330'
data['ts'] = '1592805315792'
data['bv'] = 'facd2f096bb5bf93986bf7ae3e8ceab8'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data, header)
response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')
target = json.loads(html)

print(target['translateResult'][0][0]['tgt'])
