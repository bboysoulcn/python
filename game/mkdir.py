import os
def mkdir(path):
    isExists=os.path.exists("./hello")
    if isExists==True:
        print("目录已经存在,不创建目录")
    else:
        os.mkdir(path)
        print("目录创建成功")


