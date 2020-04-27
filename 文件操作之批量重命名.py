import os
# os.mkdir('aa')    #在当前目录下创建 aa 目录
os.chdir('aa')      #进入aa目录

#以下代码是批量创建文件
# for i in range(10):                  #批量创建文件
#     f = open('./%s'%i + '.txt',"a")  ##这里的./指代的是当前文件夹, %i表示文件的名称,a表示没有该文件就新建.
#     f.write('test')
#     f.close()

#以下代码是批量重命名。 把所有的文件前面加上 'python_' 字段。
print(os.listdir())  #获取目录里所有文件名字
files = os.listdir()
# for i1 in (files):
#     new_name = 'python_' + i1    #定义新名字，加上'python_'字段。
#     os.rename(i1,new_name)   #重命名  os.rename(旧名字,新名字)
# print(os.listdir())

#以下代码是批量重命名之删除(修改)中间指定字符。
for i2 in files:
    new_name_del = i2.replace('thon','')     #replace 函数修改字符串比 切片来的舒服。 #place 位；位置；置入；放置。
    # print(new_name_del)
    os.rename(i2,new_name_del)
print(os.listdir())

# os.rename('文件操作测试模块.py','文件操作之删除.py')