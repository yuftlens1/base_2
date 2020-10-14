import os
print(os.getcwd())                        #打印出当前路径。
path = os.getcwd()                        #把当前路径附在path里方便后续操作。
print(os.listdir(path))                   #打印当前路径里的所有文件。
f = open('文件操作之read.py',encoding='UTF-8')       #打开指定文件，指定utf-8字符集
print(f.read())                                    #打印文件里内容
f.close()                                          #关闭打开的文件