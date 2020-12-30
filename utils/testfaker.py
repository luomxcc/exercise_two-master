import faker

# 初始化faker

from faker import Faker


def faker_demo():
    f = Faker(locale='zh_CN')
    print(f.address())
    print(f.time(pattern='%H:%M'))
    print(f.name())
    print(f.date_time())
    print(f.date(), '\t' + f.time(pattern='%H:%M'))


if __name__ == '__main__':
    faker_demo()

    pass
