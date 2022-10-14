import threading
from threading import  Thread ,Lock
from time import  sleep
class Account(object):

    def __init__(self):
        super().__init__()
        self._balance = 0
        self._lock = Lock()

    def change(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()
    @property
    def balance(self):
        return self._balance

if __name__ == '__main__':
    account = Account()

    t_list = []
    for i in range(100):
        t = threading.Thread(target=account.change , args= (1,))
        t_list.append(t)
        t.start()

    for i in t_list:
        i.join()

    for i, item in t_list.item():
        print(i)
        print(item)


    print('账号总额 %d' % account.balance)
