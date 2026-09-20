# Translated to Turkish by himmetcanumutlu

"""
Çok süreç ve süreç havuzunun kullanımı
Çok iş parçacığı, GIL nedeniyle CPU'nun çok çekirdekli özelliğini kullanamaz
Hesaplama yoğun görevlerde çok süreç kullanılmalıdır
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """Asal sayı mı"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    """Ana fonksiyon"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()
