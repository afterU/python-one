import atexit
from time import time, sleep
from random import randint
import _thread

def download_task(filename):
    print('开始下载%s ' % filename)
    download_time = randint(5, 10)
    print('还需要 %d 秒， 下载完成' %  download_time)
    sleep(download_time)
    print('下载完成')

def shutdown_hook(start):
    end = time()
    print('总共耗费了 %.3f 秒' % (end - start))

def main():
    start = time()
    # 多线程执行多个下载任务
    t1 = _thread.start_new_thread(download_task, ('python.pdf',))
    t2 = _thread.start_new_thread(download_task, ('java.pdf',))
    # 注册关机钩子函数， 在程序执行结束前计算执行时间
    atexit.register(shutdown_hook, start)


if __name__ == '__main__':
    main()

# # 执行这里的代码会引发致命错误(不要被这个词吓到) 因为主线程结束后下载线程再想执行就会出问题
# # 需要说明一下 由于_thread模块属于比较底层的线程操作而且不支持守护线程的概念
# # 在实际开发中会有诸多不便 因此我们推荐使用threading模块提供的高级操作进行多线程编程
