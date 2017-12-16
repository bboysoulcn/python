import requests
data = requests.get('http://www.bboysoul.com')
data.encoding='utf-8'
print(data.text)