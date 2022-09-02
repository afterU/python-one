'''
对象之间的依赖关系和运算符重载
'''

class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s 当前时速 %d' % (self._name, self._current_speed)

class Student(object):

     def __init__(self, name, age):
         self._name = name
         self._age = age

     @property
     def name(self):
         return self._name

     def drive(self, car):
         print('%s 驾驶着 %s 欢快的行驶去天安门的路上 ' % (self._name, car._brand))






