## Yıllık 500K+ Maaşlı Python Programcısı Nasıl Kod Yazar

> **Translated to Turkish by** himmetcanumutlu

### Neden Python ile Kod Yazmalı

#### Karşılaştırma Yoksa Zarar Yok

> **Birçok internet ve mobil internet işletmesi, geliştirme verimliliğine yürütme verimliliğinden daha fazla önem verir**.

##### Örnek 1: hello, world

C sürümü：

```C
#include <stdio.h>

int main() {
    printf("hello, world\n");
    return 0;
}
```

Java sürümü：

```Java
class Example01 {
    
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
```

Python sürümü：

```Python
print('hello, world')
```

#####  Örnek 2：1-100 toplamı

C sürümü：

```C
#include <stdio.h>

int main() {
    int total = 0;
    for (int i = 1; i <= 100; ++i) {
        total += i;
    }
    printf("%d\n", total);
	  return 0;
}
```

Python sürümü：

```Java
print(sum(range(1, 101)))
```

##### Örnek 3：Dizi（liste）oluşturma ve başlatma

Java sürümü：

```Java
import java.util.Arrays;

public class Example03 {

    public static void main(String[] args) {
        boolean[] values = new boolean[10];
        Arrays.fill(values, true);
        System.out.println(Arrays.toString(values));

        int[] numbers = new int[10];
        for (int i = 0; i < numbers.length; ++i) {
            numbers[i] = i + 1;
        }
        System.out.println(Arrays.toString(numbers));
    }
}
```

Python sürümü：

```Python
values = [True] * 10
print(values)
numbers = [x for x in range(1, 11)]
print(numbers)
```

##### Örnek 4：Çift renkli top rastgele numara seçimi

Java sürümü：

```Java
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

class Example03 {
    private static final List<Integer> RED_BALLS = new ArrayList<>();
    static {
        for (int i = 1; i <= 33; ++i) RED_BALLS.add(i);
    }
    
    public static void display(List<Integer> balls) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < balls.size(); i++) {
            sb.append(String.format("%02d ", balls.get(i)));
            if (i == 5) sb.append("| ");
        }
        System.out.println(sb.toString());
    }

    public static List<Integer> generate() {
        List<Integer> pool = new ArrayList<>(RED_BALLS);
        Collections.shuffle(pool);
        List<Integer> selectedBalls = pool.subList(0, 6);
        Collections.sort(selectedBalls);
        selectedBalls.add(ThreadLocalRandom.current().nextInt(1, 17));
        return selectedBalls;
    }
    
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Kaç tane rastgele seçilsin: ");
            if (sc.hasNextInt()) {
                int num = sc.nextInt();
                for (int i = 0; i < num; ++i) {
                    display(generate());
                }
            }
        }
    }
}
```

Python sürümü：

```Python
import random

RED_RANGE = range(1, 34)
BLU_RANGE = range(1, 17)


def generate():
    red_balls = random.sample(RED_RANGE, 6)
    red_balls.sort()
    blue_ball = random.choice(BLU_RANGE)
    return red_balls, blue_ball


def display(sample):
    reds, blue = sample
    reds_str = ' '.join(f'{ball:02d}' for ball in reds)
    print(f'{reds_str} | {blue:02d}')


num = int(input('Kaç tane rastgele seçilsin: '))
for _ in range(num):
    display(generate())
```

> **Sıcak hatırlatma**：Hayatınızı sevin, her türlü kumardan uzak durun.

##### Örnek 5：Basit bir HTTP sunucusu gerçekleştirme.

Java sürümü：

> **Açıklama**：JDK 1.6 öncesinde soket programlamayla gerçekleştirilmesi gerekir; somut olarak çok iş parçacıklı ve NIO olmak üzere iki yaklaşıma ayrılır. JDK 1.6 sonrasında `com.sun.net.httpserver` paketinin sağladığı `HttpServer` sınıfı kullanılabilir.

```Java
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

class Example05 {

    public static void main(String[] arg) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/", new RequestHandler());
        server.start();
    }

    static class RequestHandler implements HttpHandler {
        
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = "<h1>hello, world</h1>";
            exchange.sendResponseHeaders(200, 0);
            try (OutputStream os = exchange.getResponseBody()) {
                os.write(response.getBytes());
            }
        }
    }
}
```

Python sürümü：

```Python
from http.server import HTTPServer, SimpleHTTPRequestHandler


class RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('<h1>hello, world</h1>'.encode())


server = HTTPServer(('', 8000), RequestHandler)
server.serve_forever()
```

veya

```Python
python3 -m http.server 8000
```

#### Tek Satır Python Koduyla Neler Yapılabilir

> **Çoğu zaman sorununuz tek satır Python koduyla çözülür**.

```Python
# Tek satır kodla faktöriyel fonksiyonu gerçekleştir
fac = lambda x: __import__('functools').reduce(int.__mul__, range(1, x + 1), 1)

# Tek satır kodla en büyük ortak bölen fonksiyonunu gerçekleştir
gcd = lambda x, y: y % x and gcd(y % x, x) or x

# Tek satır kodla asal sayı belirleme fonksiyonunu gerçekleştir
is_prime = lambda x: x > 1 and not [f for f in range(2, int(x ** 0.5) + 1) if x % f == 0]

# Tek satır kodla hızlı sıralama gerçekleştir
quick_sort = lambda items: len(items) and quick_sort([x for x in items[1:] if x < items[0]]) + [items[0]] + quick_sort([x for x in items[1:] if x > items[0]]) or items

# FizzBuzz listesi üret
['Fizz'[x % 3 * 4:] + 'Buzz'[x % 5 * 4:] or x for x in range(1, 101)]
```

#### Tasarım Desenleri Hiç Bu Kadar Basit Olmamıştı

> **Python dinamik tipli bir dildir; çok sayıda tasarım deseni Python'da basitleştirilir veya zayıflatılır**.

Düşünün: Aşağıdaki kod nasıl optimize edilir.

```Python
def fib(num):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)
```

Vekil (proxy) deseni, Python'da yerleşik veya özel dekoratörlerle gerçekleştirilebilir.

```Python
from functools import lru_cache


@lru_cache()
def fib(num):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)


for n in range(1, 121):
    print(f'{n}: {fib(n)}')
```

> **Açıklama**：Python standart kütüphanesi `functools` modülünün `lru_cache` dekoratörüyle `fib` fonksiyonuna önbellek vekili eklenir; fonksiyonun ara sonuçları önbelleğe alınır ve kodun performansı optimize edilir.

Tekil (singleton) deseni, Python'da özel dekoratör veya üst sınıf (metaclass) ile gerçekleştirilebilir.

```Python
from functools import wraps
from threading import RLock


def singleton(cls):
    instances = {}
    lock = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
```

> **Açıklama**：Tekil desenini gerçekleştirmesi gereken sınıfa yalnızca yukarıdaki dekoratörün eklenmesi yeterlidir.

Prototip deseni, Python'da üst sınıf (metaclass) ile gerçekleştirilebilir.

```Python
import copy


class PrototypeMeta(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.clone = lambda self, is_deep=True: \
            copy.deepcopy(self) if is_deep else copy.copy(self)
```

> **Açıklama**：Üst sınıfla, `metaclass=PrototypeMeta` belirtilen sınıfa nesne klonlamak için bir `clone` yöntemi eklenir; Python standart kütüphanesi `copy` modülünün `copy` ve `deepcopy` fonksiyonlarıyla sırasıyla sığ ve derin kopya gerçekleştirilir.

#### Veri Toplama ve Veri Analizi Hiç Bu Kadar Basit Olmamıştı

> **Ağ veri toplama, Python'un en iyi olduğu alanlardan biridir.**

Örnek：Douban filmi "Top250"yi alma.

```Python
import random
import time

import requests
from bs4 import BeautifulSoup

for page in range(10):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={25 * page}',
        headers={'User-Agent': 'BaiduSpider'}
    )
    soup = BeautifulSoup(resp.text, "lxml")
    for elem in soup.select('a > span.title:nth-child(1)'):
        print(elem.text)
    time.sleep(random.random() * 5)
```

> **NumPy、Pandas、Matplotlib ile veri analizi ve görselleştirme kolayca gerçekleştirilebilir**.

![](res/use-pandas-in-jupyter-notebook.png)

### Python Kodu Yazmanın Doğru Duruşu

> **Python ile kod yazarken Pythonic kod yazmalısınız**.

#### Duruş 1：Seçim yapısının doğru duruşu

Diğer dillerden geçiş yapan geliştiricinin kodu：

```Python
name = 'jackfrued'
fruits = ['apple', 'orange', 'grape']
owners = {'name': '骆昊', 'age': 40, 'gender': True}
if name != '' and len(fruits) > 0 and len(owners.keys()) > 0:
    print('Jackfrued love fruits.')
```

Pythonic kod：

```Python
name = 'jackfrued'
fruits = ['apple', 'orange', 'grape']
owners = {'name': '骆昊', 'age': 40, 'gender': True}
if name and fruits and owners:
    print('Jackfrued love fruits.')
```

#### Duruş 2：İki değişkeni takas etmenin doğru duruşu

Diğer dillerden geçiş yapan geliştiricinin kodu：

```Python
temp = a
a = b
b = temp
```

veya

```Python
a = a ^ b
b = a ^ b
a = a ^ b
```

Pythonic kod：

```Python
a, b = b, a
```


#### Duruş 3：Diziyle string oluşturmanın doğru duruşu

Diğer dillerden geçiş yapan geliştiricinin kodu：

```Python
chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
name = ''
for char in chars:
    name += char
```

Pythonic kod：

```Python
chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
name = ''.join(chars)
```


#### Duruş 4：Listede gezinmenin doğru duruşu

Diğer dillerden geçiş yapan geliştiricinin kodu：

```Python
fruits = ['orange', 'grape', 'pitaya', 'blueberry']
index = 0
for fruit in fruits:
    print(index, ':', fruit)
    index += 1
```

Pythonic kod：

```Python
fruits = ['orange', 'grape', 'pitaya', 'blueberry']
for index, fruit in enumerate(fruits):
    print(index, ':', fruit)
```


#### Duruş 5：Liste oluşturmanın doğru duruşu

Diğer dillerden geçiş yapan geliştiricinin kodu：

```Python
data = [7, 20, 3, 15, 11]
result = []
for i in data:
    if i > 10:
        result.append(i * 3)
```

Pythonic kod：

```Python
data = [7, 20, 3, 15, 11]
result = [num * 3 for num in data if num > 10]
```


#### Duruş 6：Kod sağlamlığını sağlamanın doğru duruşu

Diğer dillerden geçiş yapan geliştiricinin kodu：

```Python
data = {'x': '5'}
if 'x' in data and isinstance(data['x'], (str, int, float)) \
        and data['x'].isdigit():
    value = int(data['x'])
    print(value)
else:
    value = None
```

Pythonic kod：

```Python
data = {'x': '5'}
try:
    value = int(data['x'])
    print(value)
except (KeyError, TypeError, ValueError):
    value = None
```


### Lint Araçlarıyla Kod Standardınızı Denetleyin

Aşağıdaki kodu okuyun ve hangi yerlerde kusur olduğunu veya Python programlama standardına uymadığını görebilecek misiniz bakın.

```Python
from enum import *

@unique
class Suite (Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card(object):
    def __init__(self,suite,face ):
        self.suite = suite
        self.face = face


    def __repr__(self):
        suites='♠♥♣♦'
        faces=['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

import random

class Poker(object):
    def __init__(self):
        self.cards =[Card(suite, face) for suite in Suite
            for face in range(1, 14)]
        self.current=0
    def shuffle (self):
        self.current=0
        random.shuffle(self.cards)
    def deal (self):
        card = self.cards[self.current]
        self.current+=1
        return card
    def has_next (self):
        if self.current<len(self.cards): return True
        return False

p = Poker()
p.shuffle()
print(p.cards)
```

#### PyLint'in Kurulumu ve Kullanımı

Pylint, Python kod analiz aracıdır; Python kodundaki hataları analiz eder, kod stili standardına uymayan (varsayılan kod stili PEP 8'dir) ve potansiyel sorunlu kodu bulur.

```Bash
pip install pylint
pylint [options] module_or_package
```

Pylint çıktı biçimi şöyledir.

> modül adı:satır numarası:sütun numarası:    mesaj türü    mesaj

Mesaj türleri şunlardır:

1. C - gelenek：Python programlama geleneğini (PEP 8) ihlal eden kod.
2. R - yeniden düzenleme：oldukça kötü yazılmış, yeniden düzenlenmesi gereken kod.
3. W - uyarı：kodda bulunan ama kodun çalışmasını etkilemeyen sorunlar.
4. E - hata：kodda bulunan ve kodun çalışmasını etkileyen hatalar.
5. F - ölümcül hata：Pylint'in çalışmaya devam edememesine yol açan hatalar.

Pylint komutunun yaygın parametreleri:

1. `--disable=<msg ids>` veya `-d <msg ids>`：belirtilen türdeki mesajı devre dışı bırakır.
2. `--errors-only` veya `-E`：yalnızca hataları gösterir.
3. `--rcfile=<file>`：yapılandırma dosyasını belirtir.
4. `--list-msgs`：Pylint mesaj listesini gösterir.
5. `--generate-rcfile`：yapılandırma dosyasının örneğini üretir.
6. `--reports=<y_or_n>` veya `-r <y_or_n>`：denetim raporunun üretilip üretilmeyeceği.

### Profile Araçlarıyla Kod Performansınızı Analiz Edin

#### cProfile Modülü

`example01.py`

```Python
import cProfile


def is_prime(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIter:

    def __init__(self, total):
        self.counter = 0
        self.current = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.total:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
            self.counter += 1
            return self.current
        raise StopIteration()

        
cProfile.run('list(PrimeIter(10000))')
```

Çalıştırma sonucu：

```
   114734 function calls in 0.573 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.573    0.573 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 example.py:14(__init__)
        1    0.000    0.000    0.000    0.000 example.py:19(__iter__)
    10001    0.086    0.000    0.567    0.000 example.py:22(__next__)
   104728    0.481    0.000    0.481    0.000 example.py:5(is_prime)
        1    0.000    0.000    0.573    0.573 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

#### line_profiler

Zaman performansı analiz edilecek fonksiyona bir `profile` dekoratörü ekleyin; bu fonksiyonun her satır kodunun çalıştırılma sayısı ve süresi analiz edilir.

`example02.py`

```Python
@profile
def is_prime(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIter:

    def __init__(self, total):
        self.counter = 0
        self.current = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.total:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
            self.counter += 1
            return self.current
        raise StopIteration()


list(PrimeIter(1000))
```

`line_profiler` üçüncü taraf kütüphanesini kurma ve kullanma.

```Bash
pip install line_profiler
kernprof -lv example.py

Wrote profile results to example02.py.lprof
Timer unit: 1e-06 s

Total time: 0.089513 s
File: example02.py
Function: is_prime at line 1

 #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
 1                                           @profile
 2                                           def is_prime(num):
 3     86624      43305.0      0.5     48.4      for factor in range(2, int(num ** 0.5) + 1):
 4     85624      42814.0      0.5     47.8          if num % factor == 0:
 5      6918       3008.0      0.4      3.4              return False
 6      1000        386.0      0.4      0.4      return True
```

#### memory_profiler

Bellek performansı analiz edilecek fonksiyona bir `profile` dekoratörü ekleyin; bu fonksiyonun her satır kodunun bellek kullanımı analiz edilir.

`example03.py`

```Python
@profile
def eat_memory():
    items = []
    for _ in range(1000000):
        items.append(object())
    return items


eat_memory()
```

`memory_profiler` üçüncü taraf kütüphanesini kurma ve kullanma.

```Python
pip install memory_profiler
python3 -m memory_profiler example.py

Filename: example03.py

Line #    Mem usage    Increment   Line Contents
================================================
     1   38.672 MiB   38.672 MiB   @profile
     2                             def eat_memory():
     3   38.672 MiB    0.000 MiB       items = []
     4   68.727 MiB    0.000 MiB       for _ in range(1000000):
     5   68.727 MiB    1.797 MiB           items.append(object())
     6   68.727 MiB    0.000 MiB       return items
```

### Kapsamlı Mesleki Nitelik Nasıl Oluşturulur

#### Öğrenme Özeti

1. Genel durumu anla
2. Kapsamı belirle
3. Hedefi tanımla
4. Kaynak ara
5. Öğrenme planı oluştur
6. Kaynakları ele
7. Öğrenmeye başla, yüzeysel dene (YAGNI)
8. Elle uygula, öğrenirken oyna
9. Tam hâkim ol, öğrendiğini uygula
10. Başkalarına öğretmekten keyif al, iyice özümse

#### Zaman Yönetimi

1. Odaklanmayı artır

2. Parçalı zamanı iyi değerlendir

3. Pomodoro tekniğini kullan

4. Zaman nasıl boşa harcanır

5. Harekete geçmek, harekete geçmemekten iyidir

   ![](res/action.png)


#### Önerilen Kitaplar

1. Kariyer planlama：《Yumuşak Beceriler - Kod Dışı Hayatta Kalma Rehberi》
2. Wu Jun serisi：《Dalganın Zirvesinde》、《Silikon Vadisi'nin Gizemi》、《Matematiğin Güzelliği》、……
3. Zaman yönetimi：《Daha Verimli Bir İnsan Olmak》、《Pomodoro Tekniği Görsel Rehberi》
