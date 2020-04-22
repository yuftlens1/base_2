# f1 = open('123.maq.txt','w')   #创建一个文件
# f1.write('qwerasdf')           #往里写点东西
# f1.close()

import time
time1 = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
old_name = '.txt'
file1 = old_name.rfind('.')         #rfind  查找字符串，从右边找指定字符下标。
print(file1)    #结果  7    ##从右边找到的第一个 '.'  ,然后返回其下标。

if file1 > 0:    #判断，如果只有 .后缀  的，则不执行复制。例如文件名只是 '.txt'。还有一个写法实现，看下面。
    # postfix = old_name[file1:]  #post有'后'的意思。

    print(old_name[0:file1])            #取出文件名开始下标到右边的第一个 '.'的名字字段。
    print(old_name[file1:])             #取出文件名右边的第一个 '.'的下标到结尾的名字字段。

    new_name = old_name[0:file1] + '_bak_' +time1 + old_name[file1:]
    print(new_name)

    old_f = open(old_name,'rb')    #以二进制打开，从底层打开，一般没啥问题。
    new_f = open(new_name,'wb')    #以二进制打开，以二进制写入。
    while True:                    #循环读写。
        con = old_f.read(1024)     #1024表示读取长度。每次循环读取这么长
        # con = old_f.read(1)      #1表示读取长度。
        if len(con) == 0:
            break
        new_f.write(con)          #把读到的写进来。
    new_f.close()
    old_f.close()
else:
    print(f'{old_name} 是无效文件')