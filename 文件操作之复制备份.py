import time
time1 = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
old_name = '123.maq.txt'
file1 = old_name.rfind('.')         #rfind  查找字符串，从右边找指定字符下标。
print(file1)    #结果  7    ##从右边找到的第一个 '.'  ,然后返回其下标。

print(old_name[0:file1])            #取出文件名开始下标到右边的第一个 '.'的名字字段。
print(old_name[file1:])             #取出文件名右边的第一个 '.'的下标到结尾的名字字段。

new_name = old_name[0:file1] + '_bak_' +time1 + old_name[file1:]
print(new_name)