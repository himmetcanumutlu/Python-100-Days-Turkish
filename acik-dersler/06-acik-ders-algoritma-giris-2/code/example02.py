# Translated to Turkish by himmetcanumutlu

def climb(num):
    a, b, c = 1, 2, 4
    for _ in range(num - 1):
        a, b, c = b, c, a + b + c
    return a


def main():
    n = int(input('Basamak sayısı: '))
    print(climb(n))


if __name__ == '__main__':
    main()
