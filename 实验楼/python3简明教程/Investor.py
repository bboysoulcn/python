amount = float(input("输入投资数额"))
inrate = float(input("输入投资利率"))
period = int(input("输入期限"))
value = 0
year = 1

while year < period:
    value = amount + (amount * inrate)
    print("第{}年得到{:.2f}".format(year,value))
    amount = value
    year = year +1