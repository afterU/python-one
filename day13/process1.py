'''
多进程和单进程的差异
多进程间的通讯， 通过管道，信号， 套接字， 共享内存区
'''

from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid

def download_task(filename):
    print('当前进程号 %d' % getpid())
    print('开始下载《%s》' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('《%s》下载完成！ 耗时了%d秒' % (filename, time_to_download))

def single_process():
    start = time()
    download_task('python.pdf')
    download_task('java.pdf')
    end = time()
    print('总共耗时%d', (end - start))

def multi_process():
    start = time()
    p1 = Process(target=download_task, args='python.pdf')
    p1.start()
    p2 = Process(target=download_task, args='java.pdf')
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗时%d', (end - start))




if __name__ == '__main__':
    single_process()
    multi_process()
