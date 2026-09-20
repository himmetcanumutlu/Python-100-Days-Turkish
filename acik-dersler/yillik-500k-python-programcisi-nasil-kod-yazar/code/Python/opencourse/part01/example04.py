# Translated to Turkish by himmetcanumutlu

from random import randint, sample


def generate():
    """Bir grup rastgele numara üret"""
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def display(balls):
    """Bir grup çift renkli top numarası yazdır"""
    for index, ball in enumerate(balls):
        print(f'{ball:0>2d}', end=' ')
        if index == len(balls) - 2:
            print('|', end=' ')
    print()


num = int(input('Kaç tane rastgele seçilsin: '))
for _ in range(num):
    display(generate())
