import socket

print("*************")
print(" SSH SEARCH  ")
print("*************")
port1=input("port1:")
port2=input("port2:")
ip=input("ip:")
s=socket.socket()
for port in range(int(port1),int(port2)+1):
    try:
        print(port)
        s.connect((ip,port))
        banner=s.recv(1024)
        if banner:
            print("[+] find " + str(port) + " is open")
            print(banner)
        s.close()
    except:
        pass