from bs4 import BeautifulSoup
import requests
import re

r=requests.get("https://www.85porn.com/video/21091")
soup=BeautifulSoup(r.content,"lxml")
script=soup.find_all("script")
url=re.findall(r'https://www.85porn.com/media/videos/iphone/21091.mp4?st=-C1ZYDgNuwmc2Xn_ZOxixw&e=1515380300',str(script))
print(url)


# https://www.85porn.com/media/videos/iphone/\w.mp4?st=-C1ZYDgNuwmc2Xn_ZOxixw&e=1515380300