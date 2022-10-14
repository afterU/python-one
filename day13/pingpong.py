
from time import sleep
from multiprocessing import Process, Queue
counter = 0

def sub_task(str):
    global counter
    while counter < 10:
        print(str, end=' ', flush=True)
        counter += 1
        sleep(0.01)
'''
看起来没毛病，但是最后的结果是Ping和Pong各输出了10个，Why？当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量，
所以结果也就可想而知了。要解决这个问题比较简单的办法是使用multiprocessing模块中的Queue类，它是可以被多个进程共享的队列，底层是通过管道和信号量（semaphore）机制来实现的
'''
def main():
    Process(target=sub_task, args=('ping',)).start()
    print()
    Process(target=sub_task, args=('pong',)).start()


q = Queue(maxsize=10)

def main2():
    global q
    arr = ['ping', 'pong'] * 5
    for i in arr:
        q.put(i)
    # while not q.empty():
    #     str = q.get()
    #     print(str, end=' ', flush=True)
    #     sleep(0.01)

    p1 = Process(target=sub_task2, args=())
    p1.start()
    p2 = Process(target=sub_task2, args=())
    p2.start()
    p1.join()
    p2.join()
    # Process(target=sub_task2, args=()).start()
    # Process(target=sub_task2, args=()).start()
def sub_task2():

    while not q.empty():
        if not q.empty():

            str = q.get()
            print(str, end=' ', flush=True)
            sleep(0.01)
        else:
            continue


if __name__ == '__main__':
    # main()
    main2()