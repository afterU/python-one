'''
Python 文件与IO示例
'''
import sys

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
with open('/Users/huangzw/work/xiandou/tool/dstool.sh','r', encoding='utf-8') as f:
    for line in f:
        print(line)
    # 1. 在例子程序中的with语句给被使用到的文件创建了一个上下文环境，
    # 但 with 控制块结束时，文件会自动关闭。你也可以不使用 with 语句，但是这时候你就必须记得手动关闭文件
    # 2. 另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。 默认情况下，Python会以统一模式处理换行符。
    # 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。
    # 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。 如果你不希望这种默认的处理方式，可以给 open() 函数传入参数 newline=''
with open('/Users/huangzw/work/xiandou/tool/dstool.sh','r', encoding='utf-8', newline='') as f:
    for line in f:
        print(line)
    # 3. 最后一个问题就是文本文件中可能出现的编码错误。 但你读取或者写入一个文本文件时，你可能会遇到一个编码或者解码错误, 可以使用errors指定错误的处理方式
with open('/Users/huangzw/work/xiandou/tool/dstool.sh','r', encoding='utf-8', errors='strict') as f:
    for line in f:
        print(line)

print(sys.getdefaultencoding())

# 2) 打印输出到文件中
with open('/Users/huangzw/work/xiandou/ds/1677145494988.txt', 'wt') as f:
    print("hello world", file=f)
    # 有一点要注意的就是文件必须是以文本模式打开。 如果文件是二进制模式的话，打印就会出错

# 3) 使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符
print('ACME', 50, 91.5, sep=',', end='!!\n')
    # sep 分割符， end 结尾符
    # 当输出为字符串是， 可以使用str.join() 来达到分割的目的
print(",".join(('1','2','3')))

# 4) 读写字节数据






