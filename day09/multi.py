'''
多重继承
- 通过多重继承可以给一个类的对象具备多方面能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
'''

class Father(object):
    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('%s 在打麻将' % self._name)

    def eat(self):
        print('%s在大吃大喝' % self._name)

class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s 在吃斋' % self._name)

    def chant(self):
        print('%s 正在念经' % self._name)

class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s 在细嚼慢咽' % self._name)

    def play_piano(self):
        print('%s 在弹钢琴' % self._name)

# class Son(Father, Monk, Musician):
class Son(Monk, Father, Musician):
# class Son(Musician, Monk, Father):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)

if __name__ == '__main__':
    son = Son('张三')
    son.gamble()
    son.eat()
    son.chant()
    son.play_piano()