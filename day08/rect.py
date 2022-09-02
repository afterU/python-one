'''
定义和使用矩形
'''

class Rect(object):

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    def perimeter(self):
        return (self._width + self._height) * 2

    def area(self):
        return self._height * self._width

    def __str__(self):
        '''矩形的字符串表示'''
        return '矩形[%f,%f]' % (self._width , self._height)

    def __del__(self):
        '''析构器'''
        print('矩形对象销毁了')

if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
