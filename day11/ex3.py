import sys
import time
import os

filename = input('请输入文件名：')
try:
    with open(filename) as f:
        line = f.readlines()
except FileNotFoundError as msg:
    print('无法打开文件', filename)
    print(msg)
except UnicodeDecodeError as msg:
    print('非文本文件解码')
    sys.exit()
else:
    for i in line:
        print(i.rstrip())
        time.sleep(0.5)
finally:
    print('不管发生什么我都会执行')
