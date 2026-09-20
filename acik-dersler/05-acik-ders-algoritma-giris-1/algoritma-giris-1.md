## Algoritma Giriş Serisi Ders 1 - Tekrar Tekrar

> **Translated to Turkish by** himmetcanumutlu

### Algoritmaya Genel Bakış

1. Algoritma nedir?

   Problemi çözmenin doğru yöntemi ve somut uygulama adımları.

   Örnek 1: Aralarında 50m mesafe olan iki binanın iki odasına (iki odanın da penceresi var) nasıl bir hat çekilir?

   - Bir kuş (güvercin gibi) besleyip hattı göndermek
   - Çok uzun bir çubukla hattı uzatmak
   - Bir drone (uzaktan kumandalı hava aracı) ile hattı göndermek

   Bu yöntemlerin iyi-kötü olduğu nasıl değerlendirilir? **Az para harcamak, az zahmet çekmek**!

   Örnek 2: Büyük bir sınıfta yüzlerce öğrenci oturup birlikte ders dinliyor; öğrenci sayısı hızlıca nasıl sayılır?

   Örnek 3: Liste kapsayıcısına **tersten** 100000 eleman eklemek.

   - Yöntem 1:

     ```Python
     nums = []
     for i in range(100000):
         nums.append(i)
     nums.reverse()
     ```

   - Yöntem 2:

     ```Python
     nums = []
     for i in range(100000):
         nums.insert(0, i)
     ```

   Örnek 3: Fibonacci dizisi üretmek（ilk 100 Fibonacci sayısı）.

   - Yöntem 1 - yineleme:

     ```Python
     a, b = 0, 1
     for num in range(1, 101):
         a, b = b, a + b
         print(f'{num}: {a}')
     ```

   - Yöntem 2 - özyineleme:

     ```Python
     def fib(num):
         if num in (1, 2):
             return 1
         return fib(num - 1) + fib(num - 2)
     
     
     for num in range(1, 101):
         print(f'{num}: {fib(num)}')
     ```

   - Yöntem 3 - iyileştirilmiş özyineleme:

     ```Python
     def fib(num, temp={}):
         if num in (1, 2):
             return 1
         elif num not in temp:
             temp[num] = fib(num - 1) + fib(num - 2)
         return temp[num]
     ```

   - Yöntem 4 - iyileştirilmiş özyineleme:

     ```Python
     from functools import lru_cache
     
     
     @lru_cache()
     def fib(num):
         if num in (1, 2):
             return 1
         return fib(num - 1) + fib(num - 2)
     ```

2. Algoritmanın iyi-kötü olduğu nasıl değerlendirilir?

   [Asimptotik zaman karmaşıklığı](<https://zh.wikipedia.org/wiki/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6>) ve asimptotik uzay karmaşıklığı.

3. Büyük ***O*** simgesinin anlamı?

   Bir fonksiyonun girdi ölçeğine göre büyüme hızını gösterir; fonksiyonun büyüklük mertebesi olarak da adlandırılabilir.

   | Büyük *O* simgesi       | Açıklama               | Örnek                                         |
   | --------------- | ------------------ | -------------------------------------------- |
   | $$O(c)$$        | Sabit zaman karmaşıklığı     | Bloom filtresi / hash depolama                        |
   | $$O(log_2n)$$   | Logaritmik zaman karmaşıklığı     | ikili arama (yarılama araması)                         |
   | $$O(n)$$        | Doğrusal zaman karmaşıklığı     | sıralı arama / kova sıralama                            |
   | $$O(n*log_2n)$$ | Logaritmik doğrusal zaman karmaşıklığı | ileri sıralama algoritmaları（birleştirmeli sıralama、hızlı sıralama）|
   | $$O(n^2)$$      | Kare zaman karmaşıklığı     | basit sıralama algoritmaları（seçmeli sıralama、eklemeli sıralama、kabarcık sıralama）|
   | $$O(n^3)$$      | Küp zaman karmaşıklığı     | Floyd algoritması / matris çarpımı işlemi                     |
   | $$O(2^n)$$      | Geometrik dizi zaman karmaşıklığı | Hanoi Kulesi                                       |
   | $$O(n!)$$       | Faktöriyel zaman karmaşıklığı     | gezgin satıcı problemi                               |

### Kaba Kuvvet Yöntemi

Bilgisayar biliminde, **kaba kuvvet yöntemi** veya **brute-force arama yöntemi**, problemi çözmenin çok çok sezgisel bir yoludur; bu yöntem, çözümün tüm olası adaylarını tek tek sıralayarak ve her adayın problemin tanımına uyup uymadığını kontrol ederek sonunda problemin çözümünü bulur.

Brute-force arama çok kolay uygulanır ve çözüm varsa kesinlikle bulur; ancak maliyeti aday çözümlerin sayısıyla orantılıdır; bu nedenle birçok gerçek problemde harcanan maliyet, problem ölçeği büyüdükçe hızla artar. Dolayısıyla brute-force arama, problem ölçeği sınırlıyken veya aday çözüm kümesini yönetilebilir boyuta indirebilecek bir yöntem varken kullanılabilir. Ayrıca uygulamanın basitliği hızdan daha önemli olduğunda da bu yöntem düşünülebilir.

### Klasik Örnekler

1. **Yüz para yüz tavuk** problemi: Horoz 5 yuan, tavuk 3 yuan, civciv 1 yuan 3 adet; 100 yuan ile yüz tavuk alınır; horoz, tavuk ve civcivden kaçar adet vardır?

   ```Python
   for x in range(21):
       for y in range(34):
           z = 100 - x - y
           if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
               print(x, y, z)
   ```

2. **Beş kişi balık paylaşımı** problemi：ABCDE beş kişi bir gece birlikte balık tutar; sonunda bitkin düşüp ayrı ayrı uyurlar. Ertesi gün önce A uyanır; balığı 5 parçaya böler, fazla olan 1 balığı atar, kendi payını alır; B ikinci uyanır, o da balığı 5 parçaya böler, fazla olan 1 balığı atar, kendi payını alır; ardından C、D、E sırayla uyanır ve aynı biçimde balığı böler; en az kaç balık tutmuşlardır?

   ```Python
   fish = 6
   while True:
       total = fish
       enough = True
       for _ in range(5):
           if (total - 1) % 5 == 0:
               total = (total - 1) // 5 * 4
           else:
               enough = False
               break
       if enough:
           print(fish)
           break
       fish += 5
   ```

3. **Kaba kuvvetle parola kırma**：

   ```Python
   import re
   
   import PyPDF2
   
   with open('Python_Tricks_encrypted.pdf', 'rb') as pdf_file_stream:
       reader = PyPDF2.PdfFileReader(pdf_file_stream)
       with open('dictionary.txt', 'r') as txt_file_stream:
           file_iter = iter(lambda: txt_file_stream.readline(), '')
           for word in file_iter:
               word = re.sub(r'\s', '', word)
               if reader.decrypt(word):
                   print(word)
                   break
   ```
