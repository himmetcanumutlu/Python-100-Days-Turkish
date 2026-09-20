## Python Kapsayıcı Türlerini Kullanma İpuçları

> **Translated to Turkish by** himmetcanumutlu

Python, çok zengin kapsayıcı türünde veri tipi sağlar; herkesin en aşina olduğu `list`, `tuple`, `set`, `dict` vb. Aşağıda bu türleri kullanmaya dair bazı ipuçları paylaşıyoruz; daha Pythonic kod yazmanıza yardımcı olmasını umuyoruz.

#### 1. Sözlükten En Büyüğü Almak

Sözlük nesnesinin karşılık geldiği değişken adının `my_dict` olduğunu varsayalım.

- En büyük değeri almak

    ```Python
    max(my_dict.values())
    ```

- En büyük değerin anahtarını almak

    ```Python
    max(my_dict, key=my_dict.get)
    ```

- En büyük değerin anahtarını ve değerini almak

    ```python
     max(my_dict.items(), key=lambda x: x[1])
    ```

    veya

    ```Python
    import operator
    
    max(my_dict.items(), key=operator.itemgetter(1))
    ```
    
    > **Açıklama**: Yukarıda `operator` modülünün `itemgetter` fonksiyonu kullanıldı; bu fonksiyonun işlevi aşağıda gösterilmiştir. Yukarıdaki kodda `itemgetter`, ikili demetteki 2. elemanı almamıza yardımcı olur.
    >
    > ```Python
    > def itemgetter(*items):
    >     if len(items) == 1:
    >         item = items[0]
    >         def g(obj):
    >             return obj[item]
    >     else:
    >         def g(obj):
    >             return tuple(obj[item] for item in items)
    >     return g
    > ```

#### 2. Liste Elemanlarının Görülme Sayısını Saymak

Liste nesnesinin karşılık geldiği değişken adının `my_list` olduğunu varsayalım.

```Python
{x: my_list.count(x) for x in set(my_list)}
```

veya

```Python
from itertools import groupby

{key: len(list(group)) for key, group in groupby(sorted(my_list))}
```

> **Açıklama**: `groupby` fonksiyonu, bitişik aynı elemanları bir gruba ayırır; bu nedenle önce `sorted` fonksiyonuyla sıralamak, aynı elemanları bir araya getirmek içindir.

veya

```Python
from collections import Counter

dict(Counter(my_list))
```

#### 3. Liste Elemanlarını Kesmek

Liste nesnesinin karşılık geldiği değişken adının `my_list` olduğunu varsayalım; genellikle listeyi aşağıdaki gibi kesmek akla gelir.
```Python
my_list = my_list[:i]
my_list = my_list[j:]
```

Ancak daha iyi bir yol aşağıdaki işlemi kullanmaktır; neden olduğunu dikkatlice düşünebilirsiniz.

```Python
del my_list[i:]
del my_list[:j]
```

#### 4. En Uzun Listeye Göre zip İşlemi Yapmak

Python'un yerleşik `zip` fonksiyonu bir üreteç nesnesi üretebilir; bu üreteç nesnesi iki veya daha fazla yinelenebilir nesnenin elemanlarını bir araya getirir; aşağıdaki gibidir.

```Python
list(zip('abc', [1, 2, 3, 4]))
```

Yukarıdaki kodu çalıştırdığınızda aşağıdaki gibi bir liste elde edilir; fark etmişsinizdir ki listedeki eleman sayısı `zip` fonksiyonundaki uzunluğu en küçük olan yinelenebilir nesne tarafından belirlenir; bu nedenle aşağıdaki listede yalnızca 3 eleman vardır.

```Python
[('a', 1), ('b', 2), ('c', 3)]
```

Nihai yinelenen eleman sayısının `zip` fonksiyonundaki uzunluğu en büyük olan yinelenebilir nesne tarafından belirlenmesini istiyorsanız, `itertools` modülünün `zip_longest` fonksiyonunu deneyebilirsiniz; kullanımı şöyledir.

```Python
from itertools import zip_longest

list(zip_longest('abc', [1, 2, 3, 4]))
```

Yukarıdaki kodun oluşturduğu liste nesnesi aşağıdaki gibidir.

```Python
[('a', 1), ('b', 2), ('c', 3), (None, 4)]
```

#### 5. Bir Listeyi Hızlıca Kopyalamak

Bir liste nesnesini hızlıca kopyalamak istiyorsanız dilimleme işlemiyle yapılabilir; ancak dilimleme işlemi yalnızca sığ kopya gerçekleştirir; kısacası dilimleme yeni liste nesnesi oluşturur, ama yeni listedeki elemanlar önceki listeyle paylaşılır. Derin kopya gerçekleştirmek isterseniz `copy` modülünün `deepcopy` fonksiyonunu kullanabilirsiniz.

- Sığ kopya

    ```Python
    thy_list = my_list[:]
    ```

    veya

    ```Python
    import copy
    
    thy_list = copy.copy(my_list)
    ```

- Derin kopya

    ```Python
    import copy
    
    thy_list = copy.deepcopy(my_list)
    ```

#### 6. İki veya Daha Fazla Listenin Karşılık Gelen Elemanlarına İşlem Yapmak

Python yerleşik fonksiyonlarından `map` fonksiyonu, yinelenebilir bir nesnedeki elemanlara "eşleme" işlemi uygulayabilir; bu fonksiyon, veriyi toplu işlerken çok kullanışlıdır. Ancak pek çok kişi, bu fonksiyonun birden çok yinelenebilir nesneye de uygulanabileceğini bilmez; geçilen fonksiyonla birden çok yinelenebilir nesnedeki karşılık gelen elemanlar işlenir; aşağıdaki gibidir.

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
list(map(lambda x, y: x + y, my_list, thy_list))
```

Yukarıdaki işlem aşağıdaki gibi bir liste üretir.

```Python
[13, 17, 21, 25]
```

Elbette aynı işlem, `zip` fonksiyonu ve liste üreteciyle de yapılabilir.

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
[x + y for x, y in zip(my_list, thy_list)]
```

#### 7. Listedeki Boş ve Sıfır Değerleri İşlemek

Liste nesnesinin karşılık geldiği değişken adının `my_list` olduğunu varsayalım; listede boş değer (`None`) ve sıfır değer varsa, boş ve sıfır değerleri aşağıdaki yolla kaldırabiliriz.

```Python
list(filter(bool, my_list))
```

Karşılık gelen liste üreteci söz dizimi şöyledir.

```Python
[x for x in my_list if x]
```

#### 8. İç İçe Listeden Belirtilen Sütunu Çekmek

`my_list`'in aşağıdaki gibi bir iç içe liste olduğunu varsayalım; bu iç içe liste matematikteki matrisi temsil edebilir; matrisin ilk sütunundaki elemanları çıkarıp bir liste oluşturmak istersek şöyle yazabiliriz.

```Python
my_list = [
    [1, 1, 2, 2],
    [5, 6, 7, 8],
    [3, 3, 4, 4],
]
col1, *_ = zip(*my_list)
list(col1)
```

Burada aşağıdaki gibi bir liste elde ederiz; tam olarak matrisin ilk sütunudur.

```Python
[1, 5, 3]
```

Buna benzer şekilde, matrisin ikinci sütunundaki elemanları çıkarıp bir liste oluşturmak istersek aşağıdaki gibi bir yöntem kullanabiliriz.

```Python
_, col2, *_ = zip(*my_list)
list(col2)
```

Bu noktada, matrisin transpoze işlemini gerçekleştirmek istersek yukarıdaki düşünceye göre aşağıdaki kodu yazabiliriz.

```Python
[list(x) for x in zip(*my_list)]
```

Yukarıdaki işlemden sonra aşağıdaki gibi bir liste elde ederiz.

```Python
[[1, 5, 3], 
 [1, 6, 3], 
 [2, 7, 4], 
 [2, 8, 4]]
```
