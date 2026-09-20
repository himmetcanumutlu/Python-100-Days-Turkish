# Translated to Turkish by himmetcanumutlu

"""
Değişkenlerin kapsamı ve Python'un değişken arama sırası
LEGB: Local --> Embedded --> Global --> Built-in
global - küresel değişken bildirir veya tanımlar (ya mevcut küresel kapsamdaki değişkeni doğrudan kullanır, ya da bir değişken tanımlayıp küresel kapsama koyar)
nonlocal - iç içe kapsamdaki değişkeni kullanmayı bildirir (iç içe kapsamda ilgili değişken yoksa doğrudan hata verir)
"""
x = 100


def foo():
    global x
    x = 200

    def bar():
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
