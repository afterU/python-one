import threading
import time
from threading import Thread , Lock
from time import  sleep

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def change(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            print(threading.current_thread())
            print(time.time_ns())
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyAccount(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.change(money=self._money)

if __name__ == '__main__':
    # 创建100个线程同时想一个账号转钱

    account = Account()
    t_list = []
    for i in range(100):
        t = AddMoneyAccount(account,1)
        t_list.append(t)
        t.start()
        t.join()

    # for t in t_list:
    #     t.join()

    print('账户余额 %d' % account.balance)



#
#
#
#
# from time import sleep
# from threading import Thread, Lock
#
#
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#
#     def deposit(self, money):
#         # 先获取锁才能执行后续的代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             # 这段代码放在finally中保证释放锁的操作一定要执行
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕∫
#     for t in threads:
#         t.join()
#     print('账户余额为: ￥%d元' % account.balance)
#
#
# if __name__ == '__main__':
#     main()
