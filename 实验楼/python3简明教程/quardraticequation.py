import math

a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
d = b * b - 4 * a * c

if d < 0:
    print("root 没有")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1:", x1)
    print("x2", x2)
