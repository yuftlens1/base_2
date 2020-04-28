#一般__str__() 放的都是解释说明的内容。
#print对象名字 不再输出内存地址，而是输出 __str__() 解释说明的内容。
class Washer():
    def __init__(self):
        '''
        __init__代替了之前的haier.width = 400  haier.heigth = 500 在class外添加对象(实例)属性，直接在class里添加对象(实例)属性。
        '''
        self.width = 300
        self.heigth = 400
    def print_info(self):
        print(f'haier的高度是{self.heigth}')
        print(f'haier的宽度是{self.width}')
    def __str__(self):             #如果不加__str__()，  print(对象)就会显示对象的内存地址。
        return '直接print对象了吧'

haier = Washer()        #class实例出一个对象
haier.print_info()      #调用haier对象里的print_info功能
print(haier)            #如果不加__str__()，  print(对象)就会显示对象的内存地址。