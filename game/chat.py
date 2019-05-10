from time import sleep
import requests

# s = input("请主人输入话题：")
# while True:
#     resp = requests.post("http://www.tuling123.com/openapi/api",data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": s, })
#     resp = resp.json()
#     sleep(1)
#     print('小鱼：', resp['text'])
#     s = resp['text']
#     resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
#     resp.encoding = 'utf8'
#     resp = resp.json()
#     sleep(1)
#     print('菲菲：', resp['content'])

s = input("请输入话题:")
i=1
while True:
    data={

        "key" : "8e4cbb5654e14acb8139bdf80fa83f26",
        "info" : s,
        "userid" : "bboysoul"
    }

    response = requests.post("http://www.tuling123.com/openapi/api",data)
    text=response.json()
    if i==1:
        print('张程峰: '+text['text'])
        i=0
    else:
        print('罗gay老: ' + text['text'])
        i=1
    s=text['text']