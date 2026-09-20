# Translated to Turkish by himmetcanumutlu

"""
Eş yordam (coroutine) - gerektiğinde aralarında geçiş yapılabilen, iş birliği yapan alt programlar
"""
import asyncio

from example15 import is_prime


def num_generator(m, n):
    """Belirtilen aralığın sayı üreteci"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """Asal sayı filtresi"""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """Kare eşleyici"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """Ana fonksiyon"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
	main()
