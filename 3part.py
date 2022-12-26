'''
Python 迭代器与生成器示例
'''

# 1) Python 手动遍历迭代器

def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_iter1():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')

items = [1, 2, 3]
it = iter(items)
print(next(it))

# 2) Python 代理迭代
    # Python的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象。
    # 如果你只是迭代遍历其他容器的内容，你无须担心底层是怎样实现的。你所要做的只是传递迭代请求既可

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

# 3) Python 使用生成器创建新的迭代模式
    # 实现一种新的迭代模式，使用一个生成器函数来定义它,
    # 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 跟普通函数不同的是，生成器只能用于迭代操作

def countdown(n):
     print('Starting to count from', n)
     while n > 0:
         yield n
         n -= 1
     print('Done!')

c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
# print(next(c))

# 4) Python 实现迭代器协议
    # depth_first() 方法简单直观。 它首先返回自己本身并迭代每一个子节点并 通过调用子节点的 depth_first() 方法(使用 yield from 语句)返回对应元素
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)

class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

rt = Node2(0)
ch1 = Node2(1)
ch2 = Node2(2)
rt.add_child(child1)
rt.add_child(child2)
ch1.add_child(Node2(3))
ch1.add_child(Node2(4))
ch2.add_child(Node2(5))

print('*' * 20)
for ch in rt.depth_first():
    print(ch)
# 5) Python 反向迭代
    # 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
    # 如果两者都不符合，那你必须先将对象转换为一个列表才行, 要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存。

class CountUp:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(CountUp(30)):
    print(rr)
for rr in CountUp(30):
    print(rr)
# 6) Python 带有外部状态的生成器函数
    # 关于生成器，很容易掉进函数无所不能的陷阱。 如果生成器函数需要跟你的程序其他部分打交道的话(比如暴露属性值，允许通过方法调用来控制等等)，
    # 可能会导致你的代码异常的复杂。 如果是这种情况的话，可以考虑使用上面介绍的定义类的方式。
    # 在 __iter__() 方法中定义你的生成器不会改变你任何的算法逻辑。 由于它是类的一部分，所以允许你定义各种属性和方法来供用户使用。
from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()
with open('1part.py') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

# 7) Python 迭代器切片
    # 由迭代器生成的切片对象，但是标准切片操作并不能做到
    # 函数 itertools.islice() 正好适用于在迭代器和生成器上做切片操作
    # 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)。 函数 islice()
    # 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索引位置。
    # 这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的这个事实。 所以如果你需要之后再次访问这个迭代器的话，那你就得先将它里面的数据放入一个列表中

def count(n):
    while True:
        yield n
        n += 1

c = count(10)
# c[10:20]

import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

# 8) Python 跳过可迭代对象的开始部分
    # itertools.dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。 它会返回一个迭代器对象，丢弃原有序列中直到函数返回Flase之前的所有元素，然后返回后面所有元素。
    # 可以认为是过滤器， 但是不同于过滤器的是，只对开始部分满足过滤条件的数据进行过滤
print('*' * 20)
items = ['a','a', 'b', 'c','a', 1, 4, 10, 15]
for x in itertools.dropwhile(lambda x : x == 'a', items):
    print(x)

# 9) Python 排列组合的迭代
    # 遍历一个集合中元素的所有可能的排列或组合
    # itertools.permutations() ， 它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。 也就是说通过打乱集合中元素排列顺序生成一个元组，
    # itertools.combinations() 可得到输入集合中元素的所有的组合,元素的顺序已经不重要了。 也就是说，组合 ('a', 'b') 跟 ('b', 'a') 其实是一样的(最终只会输出其中一个)
    # itertools.combinations_with_replacement() 允许同一个元素被选择多次

# 10) Python 序列上索引值迭代
    # 在迭代一个序列的同时跟踪正在被处理的元素索引
    # 内置的 enumerate() 函数可以很好的解决这个问题, 为了按传统行号输出(行号从1开始)，你可以传递一个开始参数：
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 10):
    print(idx, val)

# 11) Python 同时迭代多个序列
    # zip() 同时迭代多个序列，每次分别从一个序列中取一个元素。
    # zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中x来自a，y来自b。 一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。
    # 如果希望迭代长度跟参数中最长的序列长度一致， 可以使用itertools.zip_longest()， 短的序列响应的元素补none
    # zip() 可以接受多于两个的序列的参数。 这时候所生成的结果元组中元素个数跟输入序列个数一样
    # zip() 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 list() 函数。 zip()可以让你将它们打包并生成一个字典dict(zip(headers,values))
print('*' * 20)
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x,y)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers,values))
for entry in  s.items():
    print(entry)

# 12) Python 不同集合上元素的迭代
    # 1. a + b 操作会创建一个全新的序列并要求a和b的类型一致
    # 2. itertools.chain() 方法可以用来简化这个任务。 它接受一个可迭代对象列表作为输入，并返回一个迭代器, chian() 如果输入序列非常大的时候会很省内存。 并且当可迭代对象类型不一样的时候可以使用 chain()
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in a + b:
    print(x)
for x in itertools.chain(a, b):
    print(x)

# 13) Python 展开嵌套的序列
    # 以写一个包含 yield from 语句的递归生成器来展开嵌套序列
    # 语句 yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用
from typing import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
def flatten2(items, ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten2(x):
                yield i
        else:
            yield x
list()
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)
for x in flatten2(items):
    print(x)
    # 在上面代码中， isinstance(x, Iterable), 检查某个元素是否是可迭代的。 如果是的话， yield from 就会返回所有子例程的值。最终返回结果就是一个没有嵌套的简单序列了。

# 14) Python 顺序迭代合并后的排序迭代对象
    # 一系列排序序列，将它们合并后得到一个排序序列 heapq.merge() 可以实现
    # heapq.merge 可迭代特性意味着它不会立马读取所有序列。 这就意味着你可以在非常长的序列中使用它，而不会有太大的开销
    # 有一点要强调的是 heapq.merge() 需要所有输入序列必须是排过序
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# 15) Python 迭代器代替while无限循环
    # iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记(结尾)值作为输入参数。 当以这种方式使用的时候，它会创建一个迭代器， 这个迭代器会不断调用 callable 对象直到返回值和标记值相等为止
CHUNKSIZE = 8192
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        # process_data(data)

def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        # process_data(chunk)
        pass

# 16) Python 创建数据处理管道
    # 在调用 gen_concatenate() 函数的时候你可能会有些不太明白。 这个函数的目的是将输入序列拼接成一个很长的行序列。
    # itertools.chain() 函数同样有类似的功能，但是它需要将所有可迭代对象作为参数传入。
    # 在上面这个例子中，你可能会写类似这样的语句 lines = itertools.chain(*files) ， 这将导致 gen_opener() 生成器被提前全部消费掉。
    # 但由于 gen_opener() 生成器每次生成一个打开过的文件， 等到下一个迭代步骤时文件就关闭了，因此 chain() 在这里不能这样使用
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('log*', '/Users/huangzw/Downloads')
for x in lognames:
    print(x)