# Translated to Turkish by himmetcanumutlu

"""
Çoklu kalıtım - bir sınıfın iki veya daha fazla üst sınıfı olması
MRO - yöntem çözümleme sırası - Method Resolution Order
Elmas kalıtımı (baklava kalıtımı) ortaya çıktığında alt sınıf hangi üst sınıfın yöntemini alır
Python 2.x - derinlik öncelikli arama
Python 3.x - C3 algoritması - genişlik öncelikli aramaya benzer
"""
class A():

    def say_hello(self):
        print('Hello, A')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Hello, C')


class D(B, C):
    pass


class SetOnceMappingMixin():
    """Özel karışım (mixin) sınıfı"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """Özel sözlük"""
    pass


def main():
    print(D.mro())
    # print(D.__mro__)
    D().say_hello()
    print(SetOnceDict.__mro__)
    my_dict= SetOnceDict()
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'


if __name__ == '__main__':
    main()
