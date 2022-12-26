'''
Python 数字日期和时间示例
'''

# 1) Python 数字的四舍五入
    #  round(value, ndigits) 函数, ndigits为正数，则保留响应的位数小数进行四舍五入， 为负数，则对响应位进行四舍五入，比如-3则对百位进行四舍五入
import math


print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))
a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

# 2) Python 执行精确的浮点数运算
    # 浮点数的一个普遍问题是它们并不能精确的表示十进制数
    # decimal 模块主要用在涉及到金融的领域。 在这类程序中，哪怕是一点小小的误差在计算过程中蔓延都是不允许的。
    # 因此， decimal 模块为解决这类问题提供了方法。 当Python和数据库打交道的时候也通常会遇到 Decimal 对象，并且，通常也是在处理金融数据的时候。
    # decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍五入运算。 为了这样做，你先得创建一个本地上下文并更改它的设置
from decimal import localcontext, Decimal

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
     ctx.prec = 3
     print(a / b)

# 3) Python 数字的格式化输出
     # 将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节
     # 格式化输出单个数字的时候，可以使用内置的 format() 函数
x = 1234.56789
print(format(x, '>10.1f'))

# 4) Python 二八十六进制整数
     # 为了将整数转换为二进制、八进制或十六进制的文本串， 可以分别使用 bin() , oct() 或 hex() 函数
y = 1234
print(bin(y))
print(oct(y))
print(hex(y))
     # 如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数
print(format(y, 'b'))
print(format(y, 'o'))
print(format(y, 'x'))

# 5) Python 字节到大整数的打包与解包
     # 一个字节字符串并想将它解压成一个整数。或者，将一个大整数转换为一个字节字符串
     # 字节顺序规则(little或big)仅仅指定了构建整数时的字节的低位高位排列方式
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data,"little"))
print(int.from_bytes(data,"big"))
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# 6) Python 复数的数学运算
     # 复数可以用使用函数 complex(real, imag) 或者是带有后缀j的浮点数来指定
     # Python中大部分与数学相关的模块都能处理复数, Python的标准数学函数确实情况下并不能产生复数值
     # 如果你想生成一个复数返回结果，你必须显示的使用 cmath 模块
a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print(a.real)
print(a.imag)
print(a.conjugate())
# 7) Python 无穷大与NaN
     # Python并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)

     # 注意无穷大计算
print(a + 45)
print(a * 10)
print(10 / a)
print(a/a)
print(a+b)
     # NaN值的一个特别的地方时它们之间的比较操作总是返回False, 测试一个NaN值得唯一安全的方法就是使用 math.isnan()
d = float('nan')
e = float('nan')
print(d == e)
print(math.isnan(d))
print(math.isnan(e))

# 8) Python 分数运算
     # fractions 模块可以被用来执行包含分数的数学运算
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)
print(a.numerator) # 分子
print(a.denominator) # 分母

# 9) Python 大型数组运算
     # 涉及到数组的重量级运算操作，可以使用 NumPy 库。 NumPy 的一个主要特征是它会给Python提供一个数组对象，相比标准的Python列表而已更适合用来做数学运算
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
print(x + y)

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
     #  NumPy 中的标量运算(比如 ax * 2 或 ax + 10 )会作用在每一个元素上
     #  NumPy 数组使用了C或者Fortran语言的机制分配内存。 也就是说，它们是一个非常大的连续的并由同类型数据组成的内存区域。 所以，你可以构造一个比普通Python列表大的多的数组
     # NumPy是Python领域中很多科学与工程库的基础，同时也是被广泛使用的最大最复杂的模块。 即便如此，在刚开始的时候通过一些简单的例子和玩具程序也能帮我们完成一些有趣的事情

# 10) Python 矩阵与线性代数运算
     # NumPy 库有一个矩阵对象可以用来解决这个问题。
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
print(m.T)
print(m.I)

# 11) Python 随机选择
     # random 模块有大量的函数用来产生随机数和随机选择元素,
     # 要想从一个序列中随机的抽取一个元素，可以使用 random.choice()
     # 提取出N个不同元素的样本用来做进一步的操作，可以使用 random.sample()
     # 打乱序列中元素的顺序，可以使用 random.shuffle(), 在原来对象之上打乱
     # 生成随机整数，请使用 random.randint()
     # 为了生成0到1范围内均匀分布的浮点数，使用 random.random()
     # 如果要获取N位随机位(二进制)的整数,使用 random.getrandbits()
import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 3))
random.shuffle(values)
print(values)
print(random.randint(0, 20))
print(random.random())
# print(random.getrandbits())
     # 在 random 模块中的函数不应该用在和密码学相关的程序中。 如果你确实需要类似的功能，可以使用ssl模块中相应的函数。 比如， ssl.RAND_bytes() 可以用来生成一个安全的随机字节序列。

# 12) Python 基本的日期与时间转换
     # 时间转换，比如天到秒，小时到分钟等的转换。为了执行不同时间单位的转换和计算，请使用 datetime 模块
from datetime import timedelta, datetime
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds/3600)
print(c.total_seconds() / 3600)
now = datetime.today()
print(now)
print(now + timedelta(days=-1))
     # datetime 会自动处理闰年
a = datetime(2012,3,1)
b = datetime(2012,2,28)
print(a-b)
a = datetime(2011,3,1)
b = datetime(2011,2,28)
print(a-b)
     #  如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块
# 13) python 计算上一个周五的日期
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
print(d + relativedelta(weekday=MO))
print(d + relativedelta(weekday=MO(-1)))