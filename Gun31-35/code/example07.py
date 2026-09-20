# Translated to Turkish by himmetcanumutlu

"""
Hash özeti - dijital imza/parmak izi - tek yönlü hash fonksiyonu (ters fonksiyonu yoktur, geri döndürülemez)
Uygulama alanları:
1. Veritabanındaki kullanıcı hassas bilgilerini hash özeti olarak saklamak
2. Verinin kötü niyetle değiştirilmediğini doğrulamak için veriye imza üretmek
3. Bulut depolama hizmetlerinin anında yükleme işlevi (tekilleştirme işlevi)
"""


class StreamHasher():
    """Özet üreteci"""

    def __init__(self, algorithm='md5', size=4096):
        """Başlatma yöntemi
        @params:
            algorithm - hash özet algoritması
            size - her seferinde okunacak veri boyutu
        """
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()


    def digest(self, file_stream):
        """Onaltılık özet string'i üret"""
        # data = file_stream.read(self.size)
        # while data:
        #     self.hasher.update(data)
        #     data = file_stream.read(self.size)
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """Ana fonksiyon"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('Python-3.7.2.tar.xz', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()
