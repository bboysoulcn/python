#-*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET)
s.bind(('0.0.0.0',1240))
s.listen(1)

conn,addr = s.accept()
print("%s is connect " % str(addr))

while True:
    message = input("小明:")
    print(message)
    conn.sendall(bytes(message))
    conn.close()