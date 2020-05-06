class Frunitrue():   #创建家具信息类     #furniture家具的意思  area面积；区域的意思
    def __init__(self,name,area):
        self.name = name
        self.area = area

class Home():      #创建家class。
    def __init__(self,address,area):
        self.addr = address   #家的地址
        self.area1 = area      #面积
        self.free_area = area #剩余面积
        self.frunitrues = []  #家具列表
    def __str__(self):
        return f'房子的地理位置是{self.addr},房屋总面积是{self.area1},剩余面积是{self.free_area},家具有{self.frunitrues}'

    def add_frunitrue(self,item):
        if item.area <= self.free_area:
            self.frunitrues.append(item.name)  ##!add_frunitrue函数传入的形参是 ‘家具对象’，所以 item.name=bed.name！！！！
            self.free_area -= item.area
        else:
            print(f'{item.name}太大，剩余面积不足')

#家具对象
bed = Frunitrue('床',6)        #实例出有数据的bed对象
sofa = Frunitrue('沙发',5)     #实例出有数据的sofa对象
ball = Frunitrue('篮球场',2000)
# print(bed.area,bed.name)
# print(sofa.area,sofa.name)

#房子
jia1 = Home('北京',30)
print(jia1)    #如果直接打印对象名字则输出类里的 __str__ 函数，没有  __str__ 函数则输出对象的内存地址

jia1.add_frunitrue(bed)
print(jia1)
jia1.add_frunitrue(sofa)
print(jia1)
jia1.add_frunitrue(ball)
print(jia1)


