# Translated to Turkish by himmetcanumutlu

"""
Ölçeklenebilir sistem performansı
- Dikey ölçekleme - tek düğümün işleme gücünü artırmak
- Yatay ölçekleme - tek düğümü çok düğüme dönüştürmek (okuma-yazma ayırma/dağıtık küme)
Eş zamanlı programlama - programın yürütülmesini hızlandırır / kullanıcı deneyimini iyileştirir
Zaman alan görevler mümkün olduğunca bağımsız çalıştırılmalı, kodun diğer kısımlarını bloklamamalıdır
- Çok iş parçacıklı
1. Thread nesnesi oluşturup target ve args özniteliklerini belirleyip start yöntemiyle iş parçacığını başlatmak
2. Thread sınıfından kalıtım alıp run yöntemini yeniden yazarak iş parçacığının çalıştıracağı görevi tanımlamak
3. ThreadPoolExecutor iş parçacığı havuzu nesnesi oluşturup submit ile çalıştırılacak görevi göndermek
3. yöntemde Future nesnesinin result yöntemiyle iş parçacığının sonucu ileride alınabilir
ayrıca done yöntemiyle iş parçacığının bittiği belirlenebilir
- Çok süreçli
- Asenkron I/O
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


# class ThumbnailThread(Thread):

#     def __init__(self, infile):
#         self.infile = infile
#         super().__init__()

#     def run(self):
#         file, ext = os.path.splitext(self.infile)
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
#             outfile = f'thumbnails/{filename}_{size}_{size}.png'
#             image = Image.open(self.infile)
#             image.thumbnail((size, size))
#             image.save(outfile, format='PNG')


def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


# def main():
#     start = time.time()
#     threads = []
#     for infile in glob.glob('images/*'):
#         # t = Thread(target=gen_thumbnail, args=(infile, ))
#         t = ThumbnailThread(infile)
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()
#     end = time.time()
#     print(f'Geçen süre: {end - start} saniye')


def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        # submit yöntemi bloklamayan bir yöntemdir
        # iş iş parçacığı sayısı tükenmiş olsa bile submit yöntemi gönderilen görevi kabul eder
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        # result yöntemi bloklayan bir yöntemdir; iş parçacığı henüz bitmediyse
        # iş parçacığının sonucu geçici olarak alınamaz, kod burada bloklanır
        future.result()
    end = time.time()
    print(f'Geçen süre: {end - start} saniye')
    # shutdown da bloklamayan bir yöntemdir; ancak gönderilmiş görevler henüz bitmediyse
    # iş parçacığı havuzu çalışmayı durdurmaz; shutdown sonrasında görev gönderilirse çalışmaz ve istisna üretir
    pool.shutdown()


if __name__ == '__main__':
    main()
