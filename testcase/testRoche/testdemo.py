import json

alist = [1,2,34,5]


def paixu():
    alist=[3,2,1,5,4,9,6,7,8]
    # 外循环 len - 1 :  因为 两两比较 ,比如有10个数 我需要比较 9轮
    # 内循环: len - i -1 : 因为 两两比较 ,比如有10个数 我需要比较 9次, 第二遍的时候 只需要比较 8次,
    # 每一轮都少一次,因为每轮 都会放一个数在后面

    #             if alist[j] > alist[j+1]:     判断相邻两个数 要不要换位置

    #             temp = alist[j]
    #             alist[j] = alist[j+1]     将相邻两个数 换位置
    #             alist[j+1] = temp
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                temp = alist[j]  # 取出前一位的数字
                alist[j] = alist[j + 1] # 让前一位等于后一位的数字
                alist[j + 1] = temp # 再让后一位等于 原来前一位的数字

    print(alist)

def list_demo1():
    alist.append('what')
    print(alist)
    blist = ['set','python']
    clist = alist + blist

    print(clist)

def set_2():
    alist = {'item':'铁','file':'word'}
    blist = {'name':'jons','six':'男'}

def fun1():
    alist = []
    blist = []
    i = 0
    while i < 100:
        alist.append(i)
        i += 1
    print('alist 的值是:{}'.format(alist))
    for i in range(0,101):
        blist.append(i)
    print('blist 的值是:{}'.format(blist))


def fun2():
    alist = [i for i in range(0,51)]
    print('alist 的值是:{}'.format(alist))

def fun3():
    a_range=[0 , 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64, 81]
    blist = [x * x for x in a_range if x%2 ==0]
    print(blist)

'''
使用列表推导式生成一个[0,5,10,15,20,…50]的列表
    使用列表推导式生成一个[page1,page2,page3…page10]的列表
'''
def fun4():
    alist = [i for i in range(0,51) if i%5==0]
    print(alist)

def fun5():
    list_demo = ['小放放','大芳芳','昊昊']
    medic = {key:len(key) for key in list_demo}
    print(medic)
    na = {4:"果芽软件", 13: "guoyasoft.com"}
    newdic = {k:v for v,k in medic.items()}
    print(newdic)
    ne = {k:v for v,k in na.items() if v>10}
    print(ne)
class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sat(self):
        print(self.name+ '扣扣')
    def sleep(self):
        print(self.name + '待在家')
    def info(self):
        print('这个人的姓名%s,今年%s岁,性别是%s'%(self.name,self.age,self.sex))
        self.sat()
class Car():
    def __init__(self,name,no,speed):
        self.name = name
        self.no = no
        self.speed = speed
    def show(self):
        print(self.name,self.speed,self.no)
    def start(self):
        if self.speed ==100:
            print(self.name+'启动了')
        else:
            print(self.name+'停在这里')
    def run(self):
        print(self.name + '行驶中,车速是:'+self.speed)

    def stop(self):
        if self.speed == 0:
            print(self.name+'当前行使速度为'+self.speed)
        else:
            print('急刹')




if __name__ == '__main__':
    car = Car('奥拓','跑起来',"100")
    car.start()
    car.run()
    car.stop()
    car.show()

    pass
