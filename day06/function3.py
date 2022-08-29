'''
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

'''
# 绝对值
print(abs(-1))
# 返回除法的结果和余数
print(divmod(25, 4))
# pow
# pow(x,y)：表示x的y次幂
print(pow(2, 3))
# pow(x,y,z)：表示x的y次幂后除以z的余数。
print(pow(2, 4, 9))
#  四舍五入
print(round(5.6))
print(round(5.4))
#默认数值型参数，取值小者；
# 字符型参数，取字母表排序靠前者。
# key---可做为一个函数，用来指定取最小值的方法。
# default---用来指定最小值不存在时返回的默认值。
# arg1---字符型参数/数值型参数，默认数值型
# 1、传入多个参数取最小值（元组、列表、集合）
print(min(1,2))
# 传入可迭代对象时，取其元素最小值
print(min('2345'))
# 传入可迭代对象为空时，必须指定参数default，用来返回默认值
print(min((),default= 1))
# print(min())
# 传入命名参数key，其为一个函数，用来指定取最小值的方法（灵活运用，根据字典的键值）
print(min((1,2,3,4),key=lambda x : -x))
# 最大值， 具体用法参考min
print(max(123,1))

# sum 求和, iterable是一个必需的参数，可以保存任何 Python 可迭代对象。可迭代对象通常包含数值，但也可以包含列表或元组。
# start是一个可选参数，可以保存一个初始值。然后将该值添加到最终结果中。它默认为0.
print(sum((1,2),start=2))