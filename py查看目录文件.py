import os
print (os.getcwd())
path = os.getcwd()
print(os.listdir(path))
f = open('文件操作之read.py',encoding='UTF-8')
print(f.read())
f.close()