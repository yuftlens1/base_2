#文件和目录的操作一般需要 os 模块
import os
#文件
# os.rename('test.txt','test1.txt')       #os模块的rename函数重命名文件。
# os.remove('test1.txt')                  #os模块的remove函数删除文件


#目录
# os.mkdir('test1')       #创建test1目录
# os.rmdir('test1')       #删除test1目录
# print(os.getcwd())      #os.getcwd() 获取当前路径，shell里是pwd
# os.chdir('test1')        #进入当前目录下的test1目录里。 #改变目录路径。
# print(os.getcwd())
print(os.listdir('test1'))   #查看当前目录下的test1目录里的内容
print(os.listdir())          #查看当前目录里的内容。隐藏目录也会显示。

#os.rename 能重命名文件和目录。

