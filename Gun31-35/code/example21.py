# Translated to Turkish by himmetcanumutlu

"""
Birden çok iş parçacığının bir kaynak için yarışması - kritik kaynağı korumak - kilit (Lock/RLock)
Birden çok iş parçacığının birden çok kaynak için yarışması (iş parçacığı sayısı > kaynak sayısı) - semafor (Semaphore)
Birden çok iş parçacığının zamanlanması - iş parçacığını duraklatmak/bekleyen iş parçacığını uyandırmak - Condition
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account():
    """Banka hesabı"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """Para çek"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """Para yatır"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()
