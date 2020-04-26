import os
#以下代码是删除当前目录的 aa目录下 的所有文件。
# test1 = os.listdir('aa')     #获取aa目录里的所有文件名
# os.chdir('aa')               #进入aa目录
# for i in test1:              #删除所有文件。
#     os.remove(i)

#以下代码是删除当前目录下所有 .txt 结尾的文件。
test2 = os.listdir()
for i in test2:
    postfix = i.rfind('.')
    if '.txt' == (i[postfix:]):
        os.remove(i)
        print(f'{i}为删除文件')
    else:
        print(f'{i}为保留文件')