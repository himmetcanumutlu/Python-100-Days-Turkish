# Translated to Turkish by himmetcanumutlu

"""
Arama - sıralı arama ve ikili arama
Algoritma: problemi çözme yöntemi (adımlar)
Bir algoritmanın iyi-kötü olduğunu değerlendiren başlıca iki gösterge vardır: asimptotik zaman karmaşıklığı ve asimptotik uzay karmaşıklığı; genellikle bir algoritmanın hem zaman hem uzay karmaşıklığını aynı anda düşük tutması zordur (çünkü zaman ve uzay uzlaştırılamaz bir çelişkidir)
Asimptotik zaman karmaşıklığını göstermek için genellikle büyük O gösterimi kullanılır
O(c): sabit zaman karmaşıklığı - hash depolama / Bloom filtresi
O(log_2 n): logaritmik zaman karmaşıklığı - ikili arama
O(n): doğrusal zaman karmaşıklığı - sıralı arama
O(n * log_2 n): logaritmik doğrusal zaman karmaşıklığı - ileri sıralama algoritmaları (birleştirmeli sıralama, hızlı sıralama)
O(n ** 2): kare zaman karmaşıklığı - basit sıralama algoritmaları (kabarcık sıralama, seçmeli sıralama, eklemeli sıralama)
O(n ** 3): küp zaman karmaşıklığı - Floyd algoritması / matris çarpımı işlemi
bunlara ayrıca polinom zaman karmaşıklığı denir
O(2 ** n): geometrik dizi zaman karmaşıklığı - Hanoi Kulesi
O(3 ** n): geometrik dizi zaman karmaşıklığı
bunlara ayrıca üstel zaman karmaşıklığı denir
O(n!): faktöriyel zaman karmaşıklığı - gezgin satıcı problemi - NP
"""
from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """Sıralı arama"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """İkili arama"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """Ana fonksiyon (programın girişi)"""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['logaritmik', 'doğrusal', 'logaritmik doğrusal', 'kare', 'küp', 'geometrik dizi', 'faktöriyel']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()
