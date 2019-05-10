fahrenheit = 0
print("fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit -32) / 1.8
    print("{:10d}{:8.2f}".format(fahrenheit,celsius))
    fahrenheit = fahrenheit +25