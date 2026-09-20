# Translated to Turkish by himmetcanumutlu

"""
Açgözlü yöntem: problemi çözerken her zaman o anda en iyi görünen seçimi yapar,
en iyi çözümü kovalamaz, tatmin edici çözümü hızla bulur.
"""
class Thing(object):
    """Eşya"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """Fiyat/ağırlık oranı"""
        return self.price / self.weight


def input_thing():
    """Eşya bilgisini gir"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """Ana fonksiyon"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'Hırsız {thing.name} adlı eşyayı aldı')
            total_weight += thing.weight
            total_price += thing.price
    print(f'Toplam değer: {total_price} dolar')


if __name__ == '__main__':
    main()
