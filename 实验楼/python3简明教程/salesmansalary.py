basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
num_camera = int(input("相机的数量:"))
price_camera = float(input("相机的单价"))
salary = bonus_rate*num_camera + num_camera * price_camera * commision_rate + basic_salary
print("salary:", salary)