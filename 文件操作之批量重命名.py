import os
# os.mkdir('aa')    #在当前目录下创建 aa 目录
os.chdir('aa')      #进入aa目录

# for i in range(10):                  #批量创建文件
#     f = open('./%s'%i + '.txt',"a")  ##这里的./指代的是当前文件夹, %i表示文件的名称,a表示没有该文件就新建.
#     f.write('test')
#     f.close()

print(os.listdir())  #获取目录里所有文件名字
files = os.listdir()
for i1 in (files):
    new_name = 'python_' + i1    #定义新名字
    os.rename(i1,new_name)   #重命名  os.rename(旧名字,新名字)
print(os.listdir())