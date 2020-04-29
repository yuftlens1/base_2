# cook.time = cook.time + time   写成   cook.time += time i = i + 1    #while条件代码块下i循环着加1.  #这句可以写成 i += 1  运算符里的复合运算符。
class SweetPotato():
    def __init__(self):            #class里添加对象(实例)属性。
        self.cook_time = 0
        self.cook_status = '生的'
        self.condiments = []
    def cook(self,time):
        '''烤地瓜方法(函数)'''

