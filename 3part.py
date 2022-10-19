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