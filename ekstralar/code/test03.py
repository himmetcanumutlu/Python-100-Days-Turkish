# Translated to Turkish by himmetcanumutlu

from random import randint, sample

# Aday kırmızı topları başlat
red_balls = [x for x in range(1, 34)]
# Altı kırmızı top seç
selected_balls = sample(red_balls, 6)
# Kırmızı topları sırala
selected_balls.sort()
# Bir mavi top ekle
selected_balls.append(randint(1, 16))
# Seçilen rastgele numaraları yazdır
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
