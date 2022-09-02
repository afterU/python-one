
class Person(object):
    '''
    Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定。
    但是如果我们需要限定自定义类型的对象只能绑定某些属性，
    可以通过在类中定义\_\_slots\_\_变量来进行限定。需要注意的是\_\_slots\_\_的限定只对当前类的对象生效，对子类并不起任何作用。
    '''
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')
    '''
    之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
    比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，
    不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。如果要做到这点，
    就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
    '''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器- getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)


def main():
    person = Person('张三', 12)
    person.play()
    person.age = 22
    person.play()
    # AttributeError: can't set attribute 'name'
    # person.name = '李四'
    person._name = '李四'
    person._gender = '男'
    print(person._gender)
    person.play()
    person._is_gay = True

if __name__ == '__main__':
    main()