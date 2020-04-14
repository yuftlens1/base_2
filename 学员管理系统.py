def inf_num():                  #定义选择界面函数。
    print('请选择功能','-' * 30)
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-' * 40)

info = []      #采用大列表里放子dict，子dict里存学员信息的方法来存全部学员的信息。 #数据库

#定义1添加学员的函数。
def add_info():
    new_id = int(input('请输入新学员id:'))
    new_name = input('请输入新学员name:')
    new_tel = input('请输入新学员tel:')
    global info   #声明info是全局变量
    for i in info:   #遍历info，用于判断学员信息是否重复
        if new_id == i['id']:
            print(f'学员信息无法添加，{new_id} 该id已经存在')
            return   #返回值并退出当前函数。
        elif new_name == i['name']:
            print(f'学员信息无法添加，{new_name} 该name已经存在')
            return
        elif new_tel == i['tel']:
            print(f'学员信息无法添加，{new_tel} 该tel已经存在')
            return
    else: #for循环后就执行else，如果上面的代码块判断到重复的了，直接return退出函数了所以就不执行else了。#如果上面的代码块没判断到重复信息(没匹配执行)也就不会return。所以会执行下面的else的。
        print('添加成功')
    info_dict = {}        #经历了上面如果学员id不存在则添加到info列表里。添加info列表则先添加到子dict里。
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    info.append(info_dict)        #把子dict学员信息添加进info列表里。
    print(info)

def del_info():   #删除学员信息函数。
    del_id = input('请输入删除学员的id:')
    del_name = input('请输入删除学员的name:')
    global info
    for i in info:
        if (del_name == i['name']) and (del_id == i['id']):   #匹配数据(list里的子dict)，匹配中了就执行下面缩进的代码块。没匹配中就执行else。
            info.remove(i)
            print(f'{del_name}的信息以删除')
            return      #这里用return和break都可以，用return的话成功删除了某学员信息后不会执行下面的 print(info)，break就会执行。删除失败了也会执行下面的print(info)。
            # break       #不管是while还是for。如果这是break的话，下面的else也不会执行。  continue就会执行下面的else。
    else: #for else结构，for循环正常退出就执行else
        print('删除失败，没有匹配到一致的name和id')
    print(info)

#修改学员信息
def modify_info():
    modify_id = int(input('请输入修改学院的id:'))
    global info
    for i in info:
        if modify_id == i['id']:   ##注意：== 是在运算时使用， = 是在赋值(变量)时使用。
            i['name'] = input('请更新该id的name:')    #重新赋值
            i['tel'] = input('请更新该id的tel:')
            print(info)
            break
    else:
        print('没有该id')

def select_info():
    global info
    select_name = input('请输入查询学员的name：')
    for i in info:
        if select_name == i['name']:
            print(f"{select_name}的id是：{i['id']},tel是{i['tel']}")
            break
    else:
        print('该name不存在')

while True:      #while 1 == 1:   也是while True:  啊!!!  while True:就是直接指定了一直为真，所以一直执行下去。
#while True 语句中一定要有结束该循环的break语句，否则会一直循环下去的，因此while true 更像是类同 与 for 一样的循环。
    inf_num()    #调用选择界面函数。
    user_num = int(input('请输入功能序列:'))
    if user_num == 1:
        print('添加学员')
        add_info()
        print()
    elif user_num == 2:
        print('删除学员')
        del_info()
        print()
    elif user_num == 3:
        print('修改学员')
        modify_info()
        print()
    elif user_num == 4:
        print('查询学员')
        select_info()
        print()
    elif user_num == 5:
        print('显示所有学员')
        print(info)
        print()
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('输入参数错误，退出系统')
        break