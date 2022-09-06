'''
属性使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制
'''

class Car(object):
    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        if self.brand != None:
            return 'Car : [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)
        else:
            return 'Car : [最高时速=%d]' % (self._max_speed)

if __name__ == '__main__':
    car = Car('QQ', 120)

    print(car)
    # ValueError: Invalid max speed for car
    # car.max_speed = -100

    car.max_speed = 320
    car.brand = 'Benz'
    # 使用__slots__属性限制后下面代码将抛异常
    # car._current_speed = 20
    print(car)
    # 如果提供了删除器可以执行下面的代码
    # del car.brand
    print(car)

    print(Car.brand.fget)
    print(Car.brand.fset)
    print(Car.brand.fdel)




