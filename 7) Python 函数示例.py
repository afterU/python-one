'''
Python 函数示例
'''
import functools

from openpyxl.styles.fonts import _no_value


# 1) Python 可接受任意数量参数的函数
# 为了能让一个函数接受任意数量的位置参数，可以使用一个*参数
# rest是由所有其他位置参数组成的元组。然后我们在代码中把它当成了一个序列来进行后续的计算
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2, 3, 4))
# 为了接受任意数量的关键字参数，使用一个以**开头的参数
import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


print(make_element('item', 'Albatross', size='large', quantity=6))


# 2) Python 只接受关键字参数的函数
# 强制关键字参数1. 位置参数和关键词参数中间有一个*分割 2. 任意数量参数后面的参数为关键字参数

def recv1(maxsize, *, block):
    print(maxsize)
    print(block)
    print('Receives a message')
    pass


def recv2(*maxsize, block):
    print(maxsize)
    print(block)
    print('Receives a message')
    pass


recv1(1024, block=True)


# 3) Python 给函数参数增加元信息
# 想为这个函数的参数增加一些额外的信息，这样的话其他使用者就能清楚的知道这个函数应该怎么使用
def add(x: int, y: int) -> int:
    return x + y


help(add)
print(add.__annotations__)


# 4) Python 返回多个值的函数
# 尽管myfun()看上去返回了多个值，实际上是先创建了一个元组然后返回的
def myfun():
    return 1, 2, 3


print(myfun())


# 5) Python 定义有默认参数的函数
# 定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值
def spam(a, b=42):
    print(a, b)


spam(1)


# 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值
def spam2(a, b=None):
    if b is None:
        b = []
    print(a, b)


spam2(2)


# 如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来
def spam3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print(a, b)


spam3(2)


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

    def __str__(self):
        return ("%s , %f" % (self.name, self.n))


xx = 'aa'
yy = Info('test', 22)
l = [1]


# 对象类型，list，set， map是地址值传递， int string是值传递
def spam4(x=xx, y=yy, l=l):
    yy.n = 33
    l.append(2)
    print(x, y, l)


print(yy)
print(l)
spam4()
yy.name = '000'
l.append(33)
xx = 4
print(xx)
print(yy)
print(l)
spam4()

# 6) Python 匿名函数捕获变量值
# 用lambda定义了一个匿名函数，并想在定义时捕获到某些变量的值。
# lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))
# 让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))
# 特别在迭代序列时定义匿名函数
func = [lambda x: x + n for n in range(5)]
for f in func:
    print(f(0))
func1 = [lambda x, n=n: x + n for n in range(5)]
for f in func1:
    print(f(0))


# 7) Python 减少可调用对象的参数个数
# 需要减少某个函数的参数个数，你可以使用 functools.partial(), 只能对原函数的第一个和最后一个参数省略
def sum_test(a, b, c, d):
    return a + b + c + d


print(sum_test(1, 2, 3, 4))
sum_test_abc = functools.partial(sum_test, d=10)
print(sum_test_abc(1, 2, 3))

# 8) Python 将单方法的类转换为函数
    # 一个除 __init__() 方法外只定义了一个方法的类。为了简化代码，你想将它转换成一个函数
    # 大多数情况下，可以使用闭包来将单个方法的类转换成函数 , 你拥有一个单方法类的原因是需要存储某些额外的状态来给方法使用
    # 大部分情况下，你拥有一个单方法类的原因是需要存储某些额外的状态来给方法使用。 比如，定义UrlTemplate类的唯一目的就是先在某个地方存储模板值，以便将来可以在open()方法中使用。
    # 使用一个内部函数或者闭包的方案通常会更优雅一些。简单来讲，一个闭包就是一个函数， 只不过在函数内部带上了一个额外的变量环境。
    # 闭包关键特点就是它会记住自己被定义时的环境。 因此，在我们的解决方案中，opener() 函数记住了 template 参数的值，并在接下来的调用中使用它。
from urllib.request import urlopen
class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

# Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://10.13.15.6:8080/mrModelBux2?prevQuery={names}&inputText={fields}')
# for line in yahoo.open(names='主驾座椅温度调高3挡', fields='再调高1档'):
#     print(line.decode('utf-8'))

def url_template(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

haha = url_template('http://10.13.15.6:8080/mrModelBux2?prevQuery={names}&inputText={fields}')
for line in haha(names='主驾座椅温度调高3挡', fields='再调高1档'):
    print(line.decode('utf-8'))