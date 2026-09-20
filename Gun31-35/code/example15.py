# Translated to Turkish by himmetcanumutlu

"""
Yineleyici - __iter__ / __next__
itertools - yinelenebilir diziler üreten araç modülü
"""
import itertools

from math import sqrt


def is_prime(num):
    """Asal sayı mı"""
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIter(object):
    """Asal sayı yineleyicisi"""

    def __init__(self, min_value, max_value):
        assert 2 <= min_value <= max_value
        self.min_value = min_value - 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        self.min_value += 1
        while self.min_value <= self.max_value:
            if is_prime(self.min_value):
                return self.min_value
            self.min_value += 1
        raise StopIteration()


class FibIter(object):
    """Fibonacci sayısı yineleyicisi"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


def main():
    # for val in itertools.permutations('ABCD'):
    #     print(val)
    # for val in itertools.combinations('ABCDE', 3):
    #     print(val)
    # for val in itertools.product('maça karo kupa sinek', range(1, 14)):
    #     print(val)
    # fib_iter = FibIter(20)
    # print('===>', next(fib_iter))
    # print('===>', next(fib_iter))
    # for val in fib_iter:
    #     print(val)
    prime_iter = PrimeIter(2, 100000)
    for val in prime_iter:
        print(val)


if __name__ == '__main__':
    main()
