#文件打开                    #open('文件名','打开模式')   #打开模式:读，写，追加。
f = open('test.txt','w')    #把文件赋到f变量里，下面调用f就是调用open函数里的文件。#如果没有test.txt则新建。

#文件操作
f.write('bbb')              #覆盖写入操作,之前test.txt里的内容会被'bbb'覆盖掉。

#文件关闭
f.close()

#访问模式对文件的影响
# f1 = open('test1.txt','r')
# # print(f1)
# f1.close()                  #结果 FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'。读模式文件不存在直接报错。

f2 = open('testa.txt','a')    #a是追加，w是写，r是读。  #a和w一样，如果没有文件则会新建一个出来。
# f2.write('abc')        #第一次追加  文件内容abc
f2.write('def')          #第二次追加  文件内容abcdef
f2.close()

f3 = open('testa.txt')   #打开模式可以省略，如果省略了默认为r。
f3.close()

f4 = open('testa.txt','a')    #a是追加，w是写，r是读。  #a和w一样，如果没有文件则会新建一个出来。
# f2.write('abc')        #第一次追加  文件内容abc
f4.write('def')          #第二次追加  文件内容abcdef
f4.close()
