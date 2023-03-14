'''
Python 文件与IO示例
'''
import io
import sys
import os

# 1) python读写文本数据
    # open(file, model, encode)
    # file 文件路径
    # model模式
        # r： 只读模式///从头开始
        # w： 写模式/文件存在则打开文件/文件不存在新建文件/原有内容删除/从头开始
        # a： 追加模式/文件存在则打开文件/文件不存在新建文件/原有内容不变/从尾开始
        # r+： 读写模式///从头开始
        # w+： 写模式/文件存在则打开文件/文件不存在新建文件/原有内容删除/从头开始
        # a+： 追加模式/文件存在则打开文件/文件不存在新建文件/原有内容不变/从尾开始
    # encode 编码  sys.getdefaultencoding() 获取系统编码
with open(os.path.dirname(__file__)+'/dstool.sh','r', encoding='utf-8') as f:
    for line in f:
        print(line)
    # 1. 在例子程序中的with语句给被使用到的文件创建了一个上下文环境，
    # 但 with 控制块结束时，文件会自动关闭。你也可以不使用 with 语句，但是这时候你就必须记得手动关闭文件
    # 2. 另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。 默认情况下，Python会以统一模式处理换行符。
    # 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。
    # 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。 如果你不希望这种默认的处理方式，可以给 open() 函数传入参数 newline=''
with open(os.path.dirname(__file__)+'/dstool.sh','r', encoding='utf-8', newline='') as f:
    for line in f:
        print(line)
    # 3. 最后一个问题就是文本文件中可能出现的编码错误。 但你读取或者写入一个文本文件时，你可能会遇到一个编码或者解码错误, 可以使用errors指定错误的处理方式
with open(os.path.dirname(__file__)+'/dstool.sh','r', encoding='utf-8', errors='strict') as f:
    for line in f:
        print(line)

print(sys.getdefaultencoding())

# 2) 打印输出到文件中
with open(os.path.dirname(__file__)+'/hw.txt', 'wt') as f:
    print("hello world", file=f)
    # 有一点要注意的就是文件必须是以文本模式打开。 如果文件是二进制模式的话，打印就会出错

# 3) 使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符
print('ACME', 50, 91.5, sep=',', end='!!\n')
    # sep 分割符， end 结尾符
    # 当输出为字符串是， 可以使用str.join() 来达到分割的目的
print(",".join(('1','2','3')))

# 4) 读写字节数据
    # 使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
with open(os.path.dirname(__file__)+'/file.bin','wb') as f:
    f.write(b'hello world')
with open(os.path.dirname(__file__)+'/file.bin','rb') as f:
    print(f.read())
    # 在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。 特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串
with open(os.path.dirname(__file__)+'/file.bin','rb') as f:
    data =f.read()
    print(data[0])
    print(chr(data[0]))
t = 'hello world'
print(t[0])
    # 二进制I/O还有一个鲜为人知的特性就是数组和C结构体类型能直接被写入，而不需要中间转换为自己对象。
    # 这个适用于任何实现了被称之为”缓冲接口”的对象，这种对象会直接暴露其底层的内存缓冲区给能处理它的操作。 二进制数据的写入就是这类操作之一
import array
nums = array.array('i',[1,2,3,4])
with open(os.path.dirname(__file__)+'/array.bin','wb') as f:
    f.write(nums)
    # 很多对象还允许通过使用文件对象的 readinto() 方法直接读取二进制数据到其底层的内存中去
    # 但是使用这种技术的时候需要格外小心，因为它通常具有平台相关性，并且可能会依赖字长和字节顺序(高位优先和低位优先)
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open(os.path.dirname(__file__)+'/array.bin','rb') as f:
    f.readinto(a)
print(a)
    # Python 文件不存在才能写入
    # 可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题, 文件是二进制的，使用 xb 来代替 xt
# with open(os.path.dirname(__file__)+'/dstool.sh','xt') as f:
#     f.write('hello world')
    # 文件不存在才能写入是为了避免覆盖文件， 可以通过先判断文件是否存在
if not os.path.exists('dstool.sh'):
    with open(os.path.dirname(__file__) + '/dstool.sh', 'wt') as f:
        f.write('hello world')
else:
    print('文件存在了')
    # Python 字符串的I/O操作
    # 使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据
    # 需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用
s = io.StringIO()
s.write('hello world\n')
print('this is a test', file=s)
# 获取所有的字符流数据
print(s.getvalue())
s1 = io.StringIO('ceshi xiao ice')
print(s1.read(4))

b = io.BytesIO()
b.write(b'binary data')
print(b.getvalue())
    # Python 读写压缩文件
    # gzip 和 bz2 模块可以很容易的处理这些文件。 两个模块都为 open() 函数提供了另外的实现来解决这个问题
    # 操作二进制数据，使用 rb 或者 wb 文件模式
import gzip
with gzip.open(os.path.dirname(__file__)+'/gzip.gz', 'wt') as f:
    f.write('hello world')
    f.write('hello world')
with gzip.open(os.path.dirname(__file__)+'/gzip.gz', 'rt') as f:
    print(f.read())
import bz2
with bz2.open(os.path.dirname(__file__)+'/bz2.bz2', 'wt') as f:
    f.write('hello world')
    f.write('hello world')
with bz2.open(os.path.dirname(__file__)+'/bz2.bz2', 'rt') as f:
    print(f.read())
    # 当写入压缩数据时，可以使用 compresslevel 这个可选的关键字参数来指定一个压缩级别
    # 默认的等级是9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低
with gzip.open(os.path.dirname(__file__)+'/gzip.gz', 'wt', compresslevel=5) as f:
    f.write('hello world')
    f.write('hello world')
    # gzip.open() 和 bz2.open() 还有一个很少被知道的特性， 它们可以作用在一个已存在并以二进制模式打开的文件上
    # 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，比如套接字，管道和内存中文件等
t = open(os.path.dirname(__file__)+'/gzip.gz', 'rb')
with gzip.open(t, 'rt') as f:
    print(f.read())

    # Python 固定大小记录的文件迭代
from functools import partial

length = 2
with open(os.path.dirname(__file__) + '/dstool.sh', 'rt') as f:
    records = iter(partial(f.read, length), '')
    print('------')
    for r in records:
        print(r)
    # 这个例子中的 records 对象是一个可迭代对象，它会不断的产生固定大小的数据块，直到文件末尾。 要注意的是如果总记录大小不是块大小的整数倍的话，最后一个返回元素的字节数会比期望值少
    # iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个标记值，它会创建一个迭代器。 这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止

    # Python 读取二进制数据到可变缓冲区中
    # 使用文件对象的 readinto() 方法， 可以将数据读取到一个可变数组中
    # 文件对象的 readinto() 方法能被用来为预先分配内存的数组填充数据，甚至包括由 array 模块或 numpy 库创建的数组。
    # 和普通 read() 方法不同的是， readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回它们。 因此，你可以使用它来避免大量的内存分配操作
    # 使用 f.readinto() 时需要注意的是，你必须检查它的返回值，也就是实际读取的字节数
    # memoryview ， 它可以通过零复制的方式对已存在的缓冲区执行切片操作，甚至还能修改它的内容

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

buff = read_into_buffer(os.path.dirname(__file__) + '/dstool.sh')
print(buff)
m1 = memoryview(buff)
buff[0:5] = b'12345'
print(buff)
print(m1)

    # Python 内存映射的二进制文件
    # 使用 mmap 模块来内存映射文件
    # mmap() 返回的 mmap 对象同样也可以作为一个上下文管理器来使用， 这时候底层的文件会被自动关闭
    # memeory_map() 函数打开的文件同时支持读和写操作。 任何的修改内容都会复制回原来的文件中。 如果需要只读的访问模式，可以给参数 access 赋值为 mmap.ACCESS_READ
    # 如果你想在本地修改数据，但是又不想将修改写回到原始文件中，可以使用 mmap.ACCESS_COPY
    # 为了随机访问文件的内容，使用 mmap 将文件映射到内存中是一个高效和优雅的方法。 例如，你无需打开一个文件并执行大量的 seek() ， read() ， write() 调用， 只需要简单的映射文件并使用切片操作访问数据即可。
    # 一般来讲， mmap() 所暴露的内存看上去就是一个二进制数组对象。 但是，你可以使用一个内存视图来解析其中的数据
    # 需要强调的一点是，内存映射一个文件并不会导致整个文件被读取到内存中。 也就是说，文件并没有被复制到内存缓存或数组中。相反，操作系统仅仅为文件内容保留了一段虚拟内存。 当你访问文件的不同区域时，这些区域的内容才根据需要被读取并映射到内存区域中。 而那些从没被访问到的部分还是留在磁盘上。所有这些过程是透明的，在幕后完成！
    # 如果多个Python解释器内存映射同一个文件，得到的 mmap 对象能够被用来在解释器直接交换数据。 也就是说，所有解释器都能同时读写数据，并且其中一个解释器所做的修改会自动呈现在其他解释器中。 很明显，这里需要考虑同步的问题。但是这种方法有时候可以用来在管道或套接字间传递数据。
    # 这一小节中函数尽量写得很通用，同时适用于Unix和Windows平台。 要注意的是使用 mmap() 函数时会在底层有一些平台的差异性。 另外，还有一些选项可以用来创建匿名的内存映射区域
import mmap
def memory_map(filename, access = mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
size = 1000000
with open(os.path.dirname(__file__) + '/mmap.log','wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map(os.path.dirname(__file__) + '/mmap.log')
print(len(m))
print(m[0:10])

with memory_map(os.path.dirname(__file__) + '/mmap.log') as m:
    print(len(m))
    print(m[0:10])
print(m.closed)

    # Python 文件路径名的操作
    # 可以用路径名来获取文件名，目录名，绝对路径
path = os.path.dirname(__file__) + '/dstool.sh'
print(path)
    # 获取文件名
print(os.path.basename(path))
    # 文件所在目录
print(os.path.dirname(path))
    # 补全用户的目录
user_path = '~/me/pythonworkspace/python-one/dstool.sh'
print(os.path.expanduser(user_path))
    # Python 测试文件是否存在
os.path.exists('/etc/passwd')
    # 是否是文件
os.path.isfile('/etc/passwd')
    # 是否是文件夹
os.path.isdir('/etc/passwd')
    # 是否是连接
print(os.path.islink('/usr/local/bin/python3'))
    # 获取真实连接
print(os.path.realpath('/usr/local/bin/python3'))
    # 获取文件大小
print(os.path.getsize('/etc/passwd'))
    # 获取文件的修改日期
print(os.path.getmtime('/etc/passwd'))
    # Python 获取文件夹中的文件列表
names = os.listdir(os.path.dirname(__file__))
print(names)
names = [name for name in os.listdir(os.path.dirname(__file__))
        if os.path.isfile(os.path.join(os.path.dirname(__file__), name))]
print(names)
    # Python 增加或改变已打开文件的编码
    # 给一个以二进制模式打开的文件添加Unicode编码/解码方式， 可以使用 io.TextIOWrapper() 对象包装它
    # io.TextIOWrapper 是一个编码和解码Unicode的文本处理层， io.BufferedWriter 是一个处理二进制数据的带缓冲的I/O层， io.FileIO 是一个表示操作系统底层文件描述符的原始文件。 增加或改变文本编码会涉及增加或改变最上面的 io.TextIOWrapper 层
str = 'ceshi xiao ice'
u = io.StringIO(str)
f = io.TextIOWrapper(u, encoding='utf-8')
print(f.buffer)
    # Python 将字节写入文本文件
    # 能够通过读取文本文件的 buffer 属性来读取二进制数据
    # I/O系统以层级结构的形式构建而成。 文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个Unicode编码/解码层来创建。 buffer 属性指向对应的底层文件。如果你直接访问它的话就会绕过文本编码/解码层
# sys.stdout.write(b'Hello\n')
sys.stdout.buffer.write(b'Hello\n')




