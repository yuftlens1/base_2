# cook.time = cook.time + time   写成   cook.time += time i = i + 1    #while条件代码块下i循环着加1.  #这句可以写成 i += 1  运算符里的复合运算符。
#面向对象 :就是变量加函数的组合成class，然后把class实例化出对象进行使用。
class SweetPotato():
    def __init__(self):            #class里添加对象(实例) 属性(变量)。
        self.cook_time = 0
        self.cook_status = '生的'
        self.condiments = []
    def cook(self,time):
        '''烤地瓜方法(函数)'''
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_status = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_status = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_status = '熟了'
        elif self.cook_time <= 8:
            self.cook_status = '糊了'
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_status}'
digua1 = SweetPotato()
print(digua1)

digua1.cook(2)
print(digua1)

digua1.cook(2)
print(digua1)    #结果 '这个地瓜烤了4分钟，状态是半生不熟'    为什么和上次时间相加了，因为代码里 'self.cook_time += time'

digua1.cook(2)
print(digua1)

digua1.cook(2)
print(digua1)

digua1.cook(2)
print(digua1)

