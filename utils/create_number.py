'''
造数据，随机手机号码。随机姓名/邮件
'''

import random, datetime, time
from math import sqrt
from functools import reduce


def create_phone():
    # 第二位数
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数根据第二位书来确定
    third = {
        3: random.randint(0, 9),
        4: [4, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 后八位数随机生成
    suffix = ''
    for x in range(8):
        suffix = suffix + str(random.randint(0, 9))

    # 拼接手机号码
    phone_number = '1{}{}{}'.format(second, third, suffix)
    return phone_number


def create_email():
    __emailtype = ['163.com', 'qq.com', 'ciloud.com']
    __emailtype = ['163.com', 'qq.com', 'ciloud.com'][random.randint[0, 2]]
    print(__emailtype)


a = 10
b = 20
'''
代码: a = 5%2 那么a的值是多少?
python中判断相等 和 不相等的符号分别是什么?
现有代码如下

n1 = 5
n2 = 10
b = n1>=5
c = n1<5 or n2 >8
d = n1>3 and n2 >8
e = n1>3 and n2 >8 and n2>10
f = not n1>=5
求 b,c,d,e,f的值 分别是什么
'''


def operator_demo1(a, b):
    a = a % b
    print(a)
    n1 = 5
    n2 = 10
    b = n1 >= 5
    c = n1 < 5 or n2 > 8
    d = n1 > 3 and n2 > 8
    e = n1 > 3 and n2 > 8 and n2 > 10
    f = not n1 >= 5
    b = True
    c = False
    d = False
    e = False
    f = False


def int1str():
    a = 100
    a = str(a)
    print(type(a))


def str_join():
    age = 30
    name = '王麻子'
    job = '软件测试工程师'
    print(name + '是一个' + job)
    print(name + '今年刚满' + str(age) + '岁')
    print('%s是一个%s,今年已经%s岁了.' % (name, job, age))
    print(f'{name}不是一个好的{job},而且他已经到了{age}')
    print('有一个人叫{},而且是一个很丑的{},都已经快{}'.format(name, job, age))


def in_demo():
    alist = ['word', 'hello', 2, 'set']
    print('word' in alist)
    print('hello' not in alist)
    print('h' in alist[1])


def deng(b, a):
    b += 1
    a -= 1
    print(a)


def is_demo():
    a = '测试'
    b = '测试,工程师'
    a1 = b.strip(',')[0]
    print(id(a))
    print(id(a1))
    print(a is not a1)
    print(a == a1)


'''
alist = ['你好',5,3.4]
a= 2 in alist
b= 2 not in alist
c='你好' in alist
d='你好' not in alist

e='你' in alist[0]
f='abc' in alist[0]
a,b,c,d,e,f的值分别是什么
False True True False True False
代码如下:

n1 = 10
n1+=1
n1-=6
n1*=5
n1+=1
print(n1)
求最后n1的值是多少26

变量a 的内存地址为2073864288, 变量b的内存地址为 2073864288, 变量c 的内存地址为 2073864299
表达式:
a is b  
a is c
a not is c
a not is b
的返回值分别是?
True False True False
    '''


def judge_ab():
    alist = ['你好', 5, 3.4]
    a = 2 in alist
    b = 2 not in alist
    c = '你好' in alist
    d = '你好' not in alist

    e = '你' in alist[0]
    f = 'abc' in alist[0]
    print(a, b, c, d, e, f)


def judge_n1():
    n1 = 10
    n1 += 1
    print(n1)
    n1 -= 6
    print(n1)
    n1 *= 5
    print(n1)
    n1 += 1
    print(n1)


def inputdemo():
    aver = input('请输入aver的值: ')
    print(type(aver))


def triangle():
    a = float(input('请输入边长1:'))
    b = float(input('请输入边长2:'))
    c = float(input('请输入边长3:'))
    if a + b > c and a + c > b and b + c > a:
        print(f'可以组一个三角形,三角形的周长为:{a + b + c}')
    else:
        print('请重新启动程序,请考虑好了再输入...')


def score1():
    score = float(input('请输入分数:'))
    if score > 99:
        grade = 'S'
    elif score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score > 60:
        grade = 'E'
    else:
        grade = '不及格! 重考吧!'
    print('成绩对应的等级是:', grade)


def nestif():
    unm = int(input('\n请输入数字:\t'))
    if unm % 2 == 0:
        if unm % 3 == 0:
            print(f'你输入的:{unm},可以被2和3整除')
        else:
            print(f'你输入的:{unm},可以被2整除,不能整除3')
    else:
        if unm % 3 == 0:
            print(f'您输入的:{unm},不能被2整除,但可以被3整除.')
        else:
            print(f'您输入的:{unm},既不能整除2,也不能整除3')


def while_demo():
    a = 0
    while a < 5:
        a += 1
        print(a)


def while_demo2():
    a = 0
    while a < 5:
        if a == 3:
            a += 1
            continue
        print('这是循环的第:%s次' % (a + 1))
        a += 1
        if a == 4:
            a += 1
            break
        print('循环到这里就结束了.{}'.format(a + 1))
        a += 1


def random_demo():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入您猜想的数字:\t'))
        if answer > number:
            print('您输入的数字小于实际答案.')
            # print(answer)
        elif answer < number:
            print('您输入的数字大于实际答案.')
            # print(answer)
        else:
            print('狗子你终于猜对了.')
            break
    print('二狗你一共猜了%s次' % counter)


'''
不看答案,写出课件中的练习题:
   1.计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字
   2.使用while 循环,打印出 1到100之间 能被3 和 5 整除的数字
   3. 使用while 循环,打印出 1到100之间 能被3 和 5 整除的数字,打印4个数字后就停止循环
'''


def method_demo():
    number = 0
    counter = 0
    alist = []
    blist = []
    while number < 100:
        counter += 1
        if number % 3 == 0:
            # print(f'这个数字{number}能被3整除')
            alist.append(number)
            if counter > 4:
                break
        number += 1
        if number % 5 == 0:
            # print(f'这个数{number}能除5')
            blist.append(number)
            if counter > 4:
                break
        number += 1
    print(alist)
    print(blist)
    print('算到这里就结束吧!')


'''
不看答案,写出课件中的练习题:
求 1到50之间的偶数和
   2.求 1到100之间的奇数和
   3. 使用for 循环,打印出 1到100之间 能被3 和 5 整除的数字
   4.使用for 循环,打印出 1到100之间 能被3 和 5 整除的数字,打印4个数字后就停止循环
   '''


def for_demo():
    sum = 0
    for number in range(1, 101):
        numb = number % 2
        if numb == 1:
            sum = sum + number
            # print(number)
    print(sum)


def for_demo1():
    sum = 0
    for number in range(0, 51):
        k = number % 2
        if k == 0:
            sum = sum + number

    print(sum)


def for_demo2():
    count = 0
    alist = []
    blist = []
    for i in range(101):
        count += 1
        if i % 3 == 0:
            alist.append(i)
            if count > 4:
                continue
        if i % 5 == 0:
            blist.append(i)
            if count > 4:
                break
    print(alist, '\n', blist)


def for_list():
    alist = ['中刷', '中超', '甲级', '河南', '河南', '四川', '四川']
    blsit = []
    for u in alist:
        if u not in blsit:
            blsit.append(u)
    print(blsit)
    s = set(alist)
    print(s)


def for_demo3():
    for i in range(5):
        print(f'这是外循环:数字{i}')
        for j in range(3):
            print(f'这是内循环数字:{j}')


def list2dict():
    alist = ['小米', '华为', '苹果', '三星', 'vivo', '金立']
    adict = {}
    for i in range(len(alist)):
        v = alist[i]
        adict[i] = v
    print(adict)


'''
练习课件中的代码
现有两个列表:
alist = ['哈', '楼', 4, 5, 1, 2, 3]
blist = ['哈', '楼', 'wo', 'de', 1, 2, 3]
请使用for循环遍历列表的方式 求出两个列表的 交集(两个列表都包含的元素) 
和 差集(alist中有的元素blist中没有 和 blist中有的元素alist中没有 的元素)
'''


def distenct_demo():
    alist = ['哈', '楼', 4, 5, 1, 2, 3]
    blist = ['哈', '楼', 'wo', 'de', 1, 2, 3]
    clist = []
    dlist = []
    for i in alist:
        if i in blist:
            clist.append(i)
        if i not in blist:
            dlist.append(i)
            for i in blist:
                if i not in alist:
                    if i not in dlist:
                        dlist.append(i)
    print('alist与blist交集为:%s' % clist)
    print(f'alsit,blsit的差集为:{dlist}')


'''
有一篮鸡蛋
每次拿 4 个 最后剩1个,
每次拿5个剩4个,
每次拿6个 最后剩3个,
每次拿7个最后剩5个,
每次拿8个最后剩1个,
每次拿9个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
'''


def egg():
    for i in range(1000):
        if i % 4 == 1 and i % 5 == 4 and i % 6 == 3 and i % 7 == 5 and i % 8 == 1 and i % 9 == 0:
            print(i)


def egg1():
    for i in range(1, 1000):
        if i % 4 != 1:
            continue
        if i % 5 != 4:
            continue
        if i % 6 != 3:
            continue
        if i % 7 != 5:
            continue
        if i % 8 != 1:
            continue
        if i % 9 != 0:
            continue
        print(i)


def sum_demo():
    a = int(input('输入一个数字:\t'))
    b = int(input('输入第二个数字:\t'))
    sum = 0
    if a < b:
        for i in range(a, b):
            if i % 2 == 0:
                sum = sum + i
    elif a > b:
        for i in range(b, a):
            if i % 2 == 0:
                sum = sum + i
    else:
        print('a 和 b 相等.')
    print(sum)


def prime_demo():
    num = int(input('请输入一个数字:\t'))
    end = int(sqrt(num))
    is_prime = True
    for i in range(2, end + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%s是一个素数.' % num)
    else:
        print(f'{num}不是素数.')


def jiujiu_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i} * {j} = {i * j}\t', end='')
        print('')


def paixu():
    alist = [12, 32, 23, 45, 72, 32, 34, 77, 45, 88, 2, 3.5, 22]
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
    print(alist)


def str_from1(name, age):
    return print('{}今年出生,明年多少{}岁!'.format(name, age))


def str_from2(name='狗剩', alias='王麻子'):
    return print('%s进动物园看猴子,被猴子抓了一把,脸被猴子抓破了,然后被人叫%s' % (name, alias))


def foo(name, *args, **kwargs):
    print('name=\t', name)
    print('list=\t', args)
    print('dict=\t', kwargs)


def parameter_demo(a, b, c, aa):
    return print('{}+{}+{}+{}'.format(a, b, c, aa))


'''
写一个 匿名函数,要求有两个参数,并且 相乘
写一个 匿名函数,要求有三个参数,并且 前两个参数想加减去第三个参数
练习课件中的代码
'''


def fun1():
    sss = lambda a, b: a * b
    print('匿名函数:\t', sss(3, 4))


def fun3():
    sss = lambda a, b, c: a * b - c
    print('匿名函数:\t', sss(3, 4, 2))


def ve1():
    a1 = "print('耗子')"
    print(a1)
    eval(a1)


def fun2(a, b, test):
    return test(a, b)


def fun4(a, b):
    if a > b:
        return b
    else:
        return a


'''
 a = lambda a,b :a if a < b else b
    print(a(20,30))
    
    list1 = [1,2,3,4,5]
    a = lambda i : [x+2 for x in i]
    print(a(list1))
    list2 = ['成都','上海']
    a = (lambda l :[print(i) for j in l for i in j ])(list2)
    print(a)
    alist = [1,2,3,4,5,6]
    a = lambda y :[print(x) for x in y if x<=4]
    print(a(alist))
    练习课件中的代码
blist = [1, 2, 3, 4, 5, 6, 7]
使用匿名函数取出blist 列表中的偶数
使用匿名函数将blist 列表中的元素加10

    blist = [1, 2, 3, 4, 5, 6, 7]
    # a = lambda x :[print(i) for i in x if i%2==0 ]
    a = lambda x :[print(i+10)for i in x ]
    print(a(blist))
'''


def mend():
    alsit = [1, -2, 3, 3, -4, 5]
    print(max(alsit))
    tmp = max(alsit, key=lambda a: abs(a))
    print(tmp)


salaries = {
    'egon': 3000,
    'alex': 100000000,
    'wupeiqi': 10000,
    'yuanhao': 2000
}

info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]


def get(k):
    return salaries[k]


def max_demo1():
    print(max(salaries, key=get))
    print(max(salaries, key=lambda i: salaries[i]))
    print(max(info, key=lambda dic: int(dic['salary'])))
    # min 替换max 即可


def sorted_demo():
    key_up = sorted(salaries)  # 降序
    print(key_up)
    up_dome1 = sorted(salaries, key=lambda x: salaries[x])  # 升序
    print(up_dome1)
    down_dome2 = sorted(salaries, key=lambda x: salaries[x], reverse=True)  # 降序
    print(down_dome2)
    l = sorted(info, key=lambda dic: int(dic['salary']))  # 升序  降序加 reverse=True
    print(l)


def map_demo():
    alist = [-10, -23, 3, 22, 42]
    plus = map(lambda x: x + 8, alist)
    print(list(plus))
    names = ['nia', 'feifei', 'chuan', 'mx']
    name = map(lambda x: x + '_a', names)
    print(list(name))
    nam = map(lambda n: n + '_b' if n == 'nia' else n + 'b', names)
    print(list(nam))


'''
info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]
求info中年龄最大的人
求info中年龄最小的人
给info中的数据按年龄从小到大排序
给info中每个人的工资加1000
'''
info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]


def info_demo():
    m1 = max(info, key=lambda age: int(age['age']))
    print(m1)
    m3 = min(info, key=lambda age: int(age['age']))
    print(m3)
    m2 = sorted(info, key=lambda age: int(age['age']))
    print(m2)
    m4 = sorted(info, key=lambda dic: int(dic['age']))
    print(m4)
    # for i in info:
    #     for salary in i:
    #         salary = salary['salary'] +'1000'
    # print(info)


v1 = ['wo', 'hao', 'e']
v2 = [1, 2, 3]


def func(x, y):
    return x + y


def redus_demo():
    ru1 = reduce(func, v1)
    print(ru1)
    ru2 = reduce(lambda x, y: x + y, v1)
    print(ru2)


def redus_demo1():
    r3 = reduce(lambda x, y: x + y, v2)
    print(r3)
    r4 = reduce(lambda x, y: x * y, v2)
    print(r4)


def redus_demo2():
    print(reduce(lambda x, y: x + y, range(101)))


def f1():
    result = filter(lambda x: x > 2, [1, 2, 3, 4])
    print(type(result))
    print(list(result))


v3 = [12, 14, 22, 'what', '123', 34, 11, 2, 31]


def f2(i):
    if type(i) == int:
        return True
    return False


def f3():
    result = filter(f2, v3)
    print(list(result))
    result = filter(lambda x: True if type(x) == int else False, v3)
    print(list(result))


def f4():
    result = filter(lambda x: True if type(x) == int and x % 2 == 0 else False, v3)
    print(list(result))
    print(list(filter(lambda x: type(x) == int and x % 2 == 0, v3)))  # 偶数
    print(list(filter(lambda x: type(x) == int, v3)))  # 数字


def f5():
    salaries = {
        'egon': 3000,
        'alex': 100000000,
        'wupeiqi': 10000,
        'yuanhao': 2000
    }
    ## 大于10000的键值对
    res = filter(lambda k: salaries[k] >= 10000, salaries)
    print(list(res))

    info = [
        {'name': 'egon', 'age': '18', 'salary': '3000'},
        {'name': 'wxx', 'age': '28', 'salary': '1000'},
        {'name': 'lxx', 'age': '38', 'salary': '2000'}
    ]
    ## 工资大于1000 的字典
    res2 = filter(lambda x: int(x['salary']) > 1000, info)
    print(list(res2))


def fun11(n):
    sun = 0
    for i in range(n, n + 1):
        sun += i
    print(sun)


# def fun12(n):
#     if n > 0:
#         return n + recu(n - 1)
#     else:
#         return 0
#
#
# def fact1(n):
    # return fact_iter(n - 1)


if __name__ == '__main__':
    phone = create_phone()
    print(phone)
    fun11(10)
    pass
