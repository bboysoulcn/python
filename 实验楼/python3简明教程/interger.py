# days = int(input("输入天数："))
# months = days // 30
# days = days % 30
# print("Month:{} Days:{}".format(months,days))

days = int(input("输入天数："))
print("Months:{} Days:{}".format(*divmod(days,30)))