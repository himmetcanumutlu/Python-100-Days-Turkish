# Translated to Turkish by himmetcanumutlu

"""
Horoz 5 yuan, tavuk 3 yuan, civciv 1 yuan 3 adet; 100 yuan ile yüz tavuk alınır; horoz, tavuk ve civcivden kaçar adet vardır?
"""
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(x, y, z)
