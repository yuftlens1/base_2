old_name = '123.maq.txt'   #指定要操作的文件名
test1 = open(old_name,'r')     #在python里打开上面指定的文件，以'r'模式
print(test1)
test2 = test1.read()           #用read函数读取其中内容。
con = len(test2)
print(con)
test1.close()                  #关闭。
