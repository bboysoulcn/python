# get 请求网页
# import requests
#
# data = requests.get('http://www.bboysoul.com')
# print(data.text)

# post 请求网站
# import requests
# data = requests.post('http://www.bboysoul.com')
# print(data.text)


# 带参数传递

# import requests
# url='http://search.bilibili.com/all?'
#
# params = {'keyword':'dsfsd','from_source':'banner_search'}
# data = requests.get(url,params)
# print(data.url)
# print(data.text)

# 构造请求头

# import requests
# url='http://search.bilibili.com/all?'
# params = {'keyword':'baidu','from_source':'banner_search'}
# headers = {
#     'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
# }
# data = requests.get(url,params,headers=headers)
# print(data.url)
# print(data.text)

# 使用data提交数据

# import requests
# url = 'http://httpbin.org/post'
#
# headers = {
# 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
# }
# data={
#     'user':'admin',
#     'pass':'admin',
# }
#
# response = requests.post(url,data=data,headers=headers)
# print(response.text)

# 提交json数据

#
#  import requests
# import json
#
# url = 'http://httpbin.org/post'
# data = {
#     'user':'bboysoul',
#     'pass':'admin',
# }
# response = requests.post(url,data=json.dumps(data))
# print(response.text)
#
# import requests
#
# url = 'http://httpbin.org/post'
# data = {
#     'user': 'admin',
#     'pass': 'admin'
# }
# response = requests.post(url, json=data)
# print(response.text)

# 使用代理

#
#  import requests
# url = 'http://www.bboysoul.com/'
#
# proxies = {
#     'http':'socks5://192.168.1.100:4396',
#     'https':'127.0.0.1:1080'
# }
#
# response = requests.get(url,proxies=proxies)
# print(response.text)

# 设置请求超时

# import requests
#
# url = 'http://www.bboysoul.com/'
#
# proxies = {
#     'http':'127.3.3.1:123',
#     'https':'127.2.1.1:456',
# }
# response = requests.get(url,timeout=3,proxies=proxies)
# print(response.text)

# 使用cookie

import requests
url = 'http://httpbin.org/cookies'

cookies ={
    'domain':'httpbin.org',
}

response = requests.get(url,cookies=cookies)
print(response.text)
print(response.status_code)