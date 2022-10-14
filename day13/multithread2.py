import atexit
import threading
from time import time, sleep
from random import randint

def download_task(filename):
    print('开始下载文件 %s ' % filename)
    download_time = randint(5, 10)
    sleep(download_time)
    print('下载文件完成')

def shutdown_hook(start):
    end = time()
    print('执行任务耗时 %s' % (end - start))

def main():
    start = time()
    t1 = threading.Thread(target=download_task, args=('python.pdf',))
    t1.start()
    t2 = threading.Thread(target=download_task, args=('java.pdf',))
    t2.start()
    t1.join()
    t2.join()

    atexit.register(shutdown_hook, start)

if __name__ == '__main__':
    main()


