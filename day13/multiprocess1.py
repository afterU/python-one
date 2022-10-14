from multiprocessing import Process, Queue
from time import sleep

def sub_task(str, q):
    number = q.get()
    while number:
        print('%d : %s' % (number, str))
        sleep(0.01)
        number = q.get()

def main():
    q = Queue(10)
    for n in range(1, 10):
        q.put(n)
    Process(target=sub_task, args=('Ping',q)).start()
    Process(target=sub_task, args=('Pong',q)).start()

if __name__ == '__main__':
    main()