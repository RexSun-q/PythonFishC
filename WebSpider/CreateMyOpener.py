import urllib.request

url = '116.22.51.176:4215'
url1 = '121.40.108.76:80'

proxy_support = urllib.request.ProxyHandler({'https':url1})

opener = urllib.request.build_opener(proxy_support)

response = opener.open('https://www.whatismyipaddress.com')

html = response.read().decode('utf-8')

print(html)
