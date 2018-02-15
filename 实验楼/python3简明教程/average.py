n = int(input("请输入要输入的数字个数"))
sum = 0
count = 0
print("输入数值回车为一个")
while count < n:
    num = float(input())
    sum = sum +num
    count = count +1
average = sum / n
print("average:{:.2f}".format(average))