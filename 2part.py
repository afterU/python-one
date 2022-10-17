'''
python字符串和文本
'''

# 1) python使用多个界定符分割字符串
    # string 对象的 split() 方法只适应于非常简单的字符串分割情形， 它并不允许有多个分隔符或者是分隔符周围不确定的空格
    # 当分割符不是一个是按照一定规则的正则表达式，可以使用re.split()
    # 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组。 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
import os
import re
import textwrap
import unicodedata

line = 'asdf fjdk; afed, fjek,asdf, foo'
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
fields2 = re.split(r'(;)\s*', line)
print(fields2)
fields3 = re.split(r';', line)
print(fields3)
# 2) python字符串开头或结尾匹配
    # 检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法, 注意这个方法接收的是一个元组
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
result = [n for n in filenames if n.endswith(('.c','.h'))]
print(result)

# 3) python 用shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
    # On OS X (Mac) 返回false， On Windows 返回True
fnmatch('foo.txt', '*.TXT')
    # 平台无关， 直接按照大小写严格匹配
fnmatchcase('foo.txt', '*.TXT')
# 4) Python 字符串匹配和搜索
    # match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall()
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
pat = re.compile(r'\d+/\d+/\d+')
print(pat.match(text))
print(pat.findall(text))
pat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(pat.match('11/27/2012'))

# 5) Python 字符串搜索和替换
    # 对于简单的字面模式，直接使用 str.replace()
    # 对于复杂的模式，请使用 re 模块中的 sub() 函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
print(text)

# 6) Python 字符串忽略大小写的搜索替换
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# 7) Python 最短匹配模式 (正则表达式非贪婪模式)
    # 正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。 而你想修改它变成查找最短的可能匹配
    # 可以在模式中的*操作符后面加上?修饰符, 这样就使得匹配变成非贪婪模式
text2 = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'"(.*)"')
print(str_pat.findall(text2))
# 期望匹配的是 no. 和yes.
str_pat = re.compile(r'"(.*?)"')
print(str_pat.findall(text2))

# 8) Python 多行匹配模式
comment = re.compile(r'/\*(.*?)\*/')
text2 = '''/* this is a
... multiline comment */
... '''
print(comment.findall(text2))

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    # (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组
print(comment.findall(text2))
    # 对于简单的情况使用 re.DOTALL 标记参数工作的很好， 但是如果模式非常复杂或者是为了构造字符串令牌而将多个模式合并起来，
    # 这时候使用这个标记参数就可能出现一些问题。 如果让你选择的话，最好还是定义自己的正则表达式模式，
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))

# 9) Python 将Unicode文本标准化
    # 在Unicode中，某些字符能够用多个合法的编码表示
    # 这里的文本”Spicy Jalapeño”使用了两种形式来表示。 第一种使用整体字符”ñ”(U+00F1)，第二种使用拉丁字母”n”后面跟一个”~”的组合字符(U+0303)
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1) #Spicy Jalapeño
print(s2) #Spicy Jalapeño
print(s1 == s2)
    # 在需要比较字符串的程序中使用字符的多种表示会产生问题。 为了修正这个问题，你可以使用unicodedata模块先将文本标准化
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(t1)
    # 清除掉一些文本上面的变音符, combining() 函数可以测试一个字符是否为和音字符
print(''.join(n for n in t1 if not unicodedata.combining(n)))

# 10) Python 删除字符串中不需要的字符
    # strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作
text3 = "   111  "
print(text3.strip())

# 11) Python 审查清理文本字符串
    # 想消除整个区间上的字符或者去除变音符。 为了这样做，你可以使用经常会被忽视的 str.translate() 方法
s = 'pýtĥöñ\x0cis\tawesome\r\n'

remap = {
ord('\t') : ' ',
ord('\f') : ' ',
ord('\r') : ' '
}
a = s.translate(remap)
print(a)

# 12) Python 字符串对齐
    # 对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center() 方法
text = 'hello world'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.ljust(20,'='))
print(text.rjust(20,'='))
print(text.center(20,'='))
    # 函数 format() 同样可以用来很容易的对齐字符串。 你要做的就是使用 <,> 或者 ^ 字符后面紧跟一个指定的宽度
print(format(text, '>20'))
print(format(text, '#^20'))
    # 在老的代码中，你经常会看到被用来格式化文本的 % 操作符。比如：
print('%-20s' % text)
print('%+20s' % text)

# 13) Python 合并拼接字符串
    # join()方法合并序列或者迭代器中的元素， + 拼接字符串， 或者将两个字符串放在一行可以省略+
    # 区别： 当我们使用加号(+)操作符去连接大量的字符串的时候是非常低效率的， 因为加号连接会引起内存复制以及垃圾回收操作。 特别的，你永远都不应像下面这样写字符串连接代码：
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s = ''
for p in parts:
    s += p
    # 这种写法会比使用 join() 方法运行的要慢一些，因为每一次执行+=操作的时候会创建一个新的字符串对象。 你最好是先收集所有的字符串片段然后再将它们连接起来。

# 14) Python 字符串中插入变量
s = '{name} has {n} messages.'
    # 14.1) format() 替换字符串中的变量
print(s.format(name='zhangsan', n=30))
    # 14.2) format_map() 和 vars() , 要替换的变量必须能在变量域中找到，否则报错
name = 'lisi'
n = 10
print(s.format_map(vars()))
    # 另外vars() 也适用于对象
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('wangwu', 12)
print(s.format_map(vars(a)))
    # format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况
    # 一种避免这种错误的方法是另外定义一个含有 __missing__() 方法的字典对象
class safesub(dict):
    def __missing__(self, key):
        return '{'+key+'}'
del n
print(s.format_map(safesub(vars())))
    # 14.3) 字符串格式化
name = 'Guido'
num = 37
sss = '%(name)    have  messages.' % vars()
print(sss)
    # 14.4) 字符串模版方式
import string
s = string.Template('$name has $num messages.')
print(s.substitute(vars()))
# 15) Python 以指定列宽格式化字符串
    # textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端大小的时候。 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s,70))
print(textwrap.fill(s,20, initial_indent=' '))
# print(textwrap.fill(s, os.get_terminal_size()))

# 16) Python 在字符串中处理html和xml
    # 你想将HTML或者XML实体如 &entity; 或 &#code; 替换为对应的文本
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.unescape(s))