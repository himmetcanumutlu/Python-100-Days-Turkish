# Translated to Turkish by himmetcanumutlu

# Tek satır kodla faktöriyel fonksiyonu
fac = lambda x: __import__('functools').reduce(int.__mul__, range(1, x + 1), 1)
print(fac(5))

# Tek satır kodla en büyük ortak bölen fonksiyonu
gcd = lambda x, y: y % x and gcd(y % x, x) or x
print(gcd(15, 27))

# Tek satır kodla asal sayı belirleme fonksiyonu
is_prime = lambda x: x > 1 and not [f for f in range(2, int(x ** 0.5) + 1) if x % f == 0]
for num in range(2, 100):
    if is_prime(num):
        print(num, end=' ')
print()

# Tek satır kodla hızlı sıralama
quick_sort = lambda items: len(items) and quick_sort([x for x in items[1:] if x < items[0]]) \
                           + [items[0]] + quick_sort([x for x in items[1:] if x > items[0]]) \
                           or items
items = [57, 12, 35, 68, 99, 81, 70, 22]
print(quick_sort(items))

# FizzBuzz listesi üret
# 1 2 Fizz 4 Buzz 6 ... 14 ... FizzBuzz 16 ... 100
print(['Fizz'[x % 3 * 4:] + 'Buzz'[x % 5 * 4:] or x for x in range(1, 101)])
