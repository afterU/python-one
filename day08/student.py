class Student(object):

    # __init__ 是一个特殊的方法用于在创建对象的时候进行初始化操作
    # 通过这个方法可以为学生对象绑定一些属性
    def __init__(self, name, age, money = 0):
        self.name = name
        self.age = age
        # 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
        self.__money = money
        # Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来“妨碍”对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们
        # 例如Student的私有属性，就可以通过 stu1._Student__money访问到

        # 在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
        # 本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
    def study(self, course_name):
        print('%s 正在学习 %s' % (self.name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s 只能观看《熊出没》' % self.name)
        else:
            print('%s 正在观看岛国爱情动作片' % self.name)
    def __private(self):
        print('私有方法被调用')

    # 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。

    def getMoney(self):
        return self.__money



def main():
    stu1 = Student('张赞', 10)
    stu1.study('Python')
    stu1.watch_av()
    print(stu1.name)
    print(stu1.getMoney())
    # AttributeError: 'Student' object has no attribute '__money'
    # print(stu1.__money)
    print(stu1._Student__money)
    # AttributeError: 'Student' object has no attribute '__private'
    # print(stu1.__private())
    print(stu1._Student__private())
    stu2 = Student('王武', 38)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()

