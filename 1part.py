'''
python 数据结构和算法
'''
# 1) Python 解压序列赋值给多个变量
    # 任何的序列（或者是可迭代对象,列表/元组/字符串/文件对象/迭代器/生成器）可以通过一个简单的赋值语句解压并赋值给多个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
import collections

p = (4, 5)
v1, v2 = p
print(p)
print(v1)
print(v2)
    # 你可能只想解压一部分，丢弃其他的值。你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares)
print(price)

# 2) Python 解压可迭代对象赋值给多个变量
    # 一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError,
    # Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候，
    # 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值，
    # 但如果有 24 个呢？这时候星号表达式就派上用场了
def drop_first_last(grades):
    first,*middle,last = grades
    #无论middle最终是0个元素还是n个元素， middle都是list类型
    return round(sum(middle)/len(middle), 1)

    # 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ， 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields,_,ign, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

def search(lines, pattern, history=5):
    previous_lines = collections.deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'9)Python 元编程示例.py') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

