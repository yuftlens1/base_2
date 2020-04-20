#文件操作之read读函数。
f = open('testa.txt')
print(f)        #结果 <_io.TextIOWrapper name='testa.txt' mode='r' encoding='cp936'>
# print(f.read()) #结果 abcdefdef ，这才是文件里的内容
# print(f.read(2))  #打印文件内容里的前两个字符。
print(f.read(11))   #文件内容read如果换行，默认换行符 /n 也是要占一个字符的。
f.close()

#文件操作之readlines读函数。  #按行读取文件内容，返回一个list，每一行就是一个数据元素。
f2 = open('testa.txt')
print(f2.readlines())                 #结果 ['abcdefdef\n', 'qq'] #qq之后没有下一行了，也就没有换行符了。
f2.close()

print(open('testa.txt').readlines())  #结果 ['abcdefdef\n', 'qq'] #qq之后没有下一行了，也就没有换行符了。

#文件操作之readline读函数。 #只读取文件内容的一行。
print(open('testa.txt').readline())   #结果 abcdefdef ，没有下一行qq。

f3 = open('testa.txt')
print(f3.readline())      #读取第一行
print(f3.readline())      #读取第二行
f3.close()


