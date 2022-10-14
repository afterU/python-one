from random import randint
from threading import Thread, current_thread, enumerate
from time import time, sleep

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下载完成！ 耗时%d秒' % (filename, time_to_download))

def main():
    start = time()
    t1 = Thread(target=download, args=('python.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('java.pdf',))
    t2.start()
    print(current_thread())
    print(enumerate())
    t1.join()
    t2.join()
    end = time()
    print('下载完成， 耗时%d' % (end - start))

if __name__ == '__main__':
    main()