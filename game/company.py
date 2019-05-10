# -*- coding:utf-8 -*-
while 1:
    i = input('输入当月利润:')
    if i == 'exit' or i == 'quit':
        break
    elif i == "":
        continue
    else:
        i = int(i)
        if (i <= 10):
            i = i * 0.1
        elif (i > 10 and i <= 20)
            i=0.1*i+(i-10)*0.075
        elif
