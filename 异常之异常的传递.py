#len() 方法返回对象（字符、列表、元组等）长度或项目个数.
import time
try:
    f = open('test.txt')
    # 尝试循环读取文件行内容
    try:
        while True:
            time.sleep(3)         #三秒一循环。
            con = f.readline()    #按行读取
            print(len(con))       #打印出每一行的长度，空行是1，我觉得这个1是 换行符 。
            if len(con) == 0:     #len() 方法返回对象（字符、列表、元组等）长度或项目个数.
                break             #如果某一行的长度为0则退出
            print(con)            #因为上面time.sleep(3)#三秒一循环。也就导致这里三秒一输出了。
    except:
        print('读取失败,程序意外终止')
        #c:\users\yufan\appdata\local\programs\python\Python37\python.exe C:\Users\YuFan\PycharmProjects\base_2\异常之异常的传递.py
except:
    print('该文件不存在')
    # open('test.txt','w')