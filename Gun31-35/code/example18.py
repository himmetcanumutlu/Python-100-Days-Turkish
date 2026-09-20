# Translated to Turkish by himmetcanumutlu

"""
Meta - üst
Üst veri - veriyi tanımlayan veri - metadata
Üst sınıf - sınıfı tanımlayan sınıf - metaclass - type'tan kalıtım alır
"""
import threading


class SingletonMeta(type):
    """Özel üst sınıf"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """Başkan (tekil sınıf)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """Ana fonksiyon"""
    p1 = President('Trump', 'ABD')
    p2 = President('Obama', 'ABD')
    p3 = President.__call__('Clinton', 'ABD')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


if __name__ == '__main__':
    main()
