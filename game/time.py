import time
now_time=time.localtime()
print(now_time.tm_mon)
print(time.time())
print(time.strftime('%Y',time.localtime()))
