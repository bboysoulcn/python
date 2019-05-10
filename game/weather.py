import requests
import tkinter


def weather(addr):
    data = {

        'key' : '8e4cbb5654e14acb8139bdf80fa83f26',
        'info' : addr+'天气',
        'userid':'bboysoul'
    }
    response = requests.post('http://www.tuling123.com/openapi/api',data)
    response = response.json()
    text = tkinter.Label(master=tk,text=response['text'])
    text.pack()



# addr = input("输入查询地址")
# weather(addr)

tk = tkinter.Tk()
tk.title('天气查询')
label = tkinter.Label(master=tk,text='输入要查询的地区')
label.pack()
entry = tkinter.Entry(master=tk)
entry.pack()
button = tkinter.Button(master=tk,text='点击查询',command = weather(entry.get()))
button.pack()
tk.mainloop()