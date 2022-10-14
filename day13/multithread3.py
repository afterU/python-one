import random
import threading
from time import time, sleep


class DownLoad_Task(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载 《%s》' % self._filename)
        download_time = random.randint(5, 10)

        print('需要下载 %d 秒' % download_time)
        sleep(download_time)
        print('《%s》 下载完成' % self._filename)

def main():
    start = time()
    t1 = DownLoad_Task('python.pdf')
    t2 = DownLoad_Task('java.pdf')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗时 %.3f 秒' % (end - start))

if __name__ == '__main__':
    main()
