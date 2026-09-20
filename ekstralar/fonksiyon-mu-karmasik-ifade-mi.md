## Fonksiyon mu, Karmaşık İfade mi?

> **Translated to Turkish by** himmetcanumutlu

Perl dilinin orijinal yazarı *Larry Wall* bir keresinde büyük programcıların üç erdemi olduğunu söylemişti: tembellik, çabuk sinirlenme ve kibir. İlk bakışta bu üç kelimeden hiçbiri olumlu değildir; ancak programcıların dünyasında bu üç kelimenin farklı anlamları vardır. Birincisi, tembellik programcıyı, kendisinin veya başkalarının işini daha iyi yapmasına yardımcı olacak zahmetten kaçıran programlar yazmaya iter; böylece tekrarlayan ve zahmetli işleri yapmak zorunda kalmayız; aynı şekilde 3 satır kodla çözülebilen bir işi asla 10 satırla yazmayız. İkincisi, çabuk sinirlenme programcıyı sizin henüz dile getirmediğiniz işleri proaktif biçimde tamamlamaya, kodunu daha verimli olacak şekilde optimize etmeye iter; 3 saniyede tamamlanabilen bir görev için asla 1 dakikalık beklemeye tahammül edemeyiz. Son olarak, kibir programcıyı güvenilir ve hatasız kod yazmaya iter; kodu eleştiri ve suçlama almak için değil, başkalarının hayran kalması için yazarız.

O zaman tartışmaya değer ilginç bir soru var: Girilen üç sayıdan en büyüğünü bulan bir programa ihtiyacımız olsun. Bu program, programlamayı bilen herkes için çocuk oyuncağıdır; hatta programlamayı bilmeyen biri 10 dakikalık bir öğrenmeyle bile halleder. Aşağıda bu sorunu çözen Python kodu var.

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
	the_max = a
else:
	the_max = b
if c > the_max:
	the_max = c
print('The max is:', the_max)
```

Ama az önce söylediğimiz gibi programcılar tembeldir; pek çok programcı yukarıdaki kodu üçlü koşul operatörüyle yeniden yazar.

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
the_max = a if a > b else b
the_max = c if c > the_max else the_max
print('The max is:', the_max)
```

Belirtmek gerekir ki Python 2.5 sürümünden önce, yukarıdaki kodun 4. ve 5. satırlarında kullanılan üçlü koşul operatörü yoktu; bunun nedeni Guido van Rossum'un (Python'un babası) üçlü koşul operatörünün Python'u daha sade hale getirmeye yardımcı olmadığını düşünmesiydi; bu nedenle C/C++ veya Java'da üçlü koşul operatörü kullanmaya alışkın olan programcılar (bu dillerde üçlü koşul operatörü "Elvis operatörü" olarak da adlandırılır; çünkü `?:` yan yana gelince ünlü rock şarkıcısı Elvis'in arkaya taralı saçına çok benzer), `and` ve `or` operatörlerinin kısa devre özelliğini kullanarak üçlü operatörü taklit etmeye çalıştılar; o dönemde yukarıdaki kod şöyle yazılırdı.

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
the_max = a > b and a or b
the_max = c > the_max and c or the_max
print('The max is:', the_max)
```

Ancak bu yaklaşım bazı senaryolarda işe yaramaz; aşağıdaki koda bakalım.

```Python
a = 0
b = -100
# Aşağıdaki kodun a'nın değerini çıktılaması beklenirdi, ancak b'nin değerini aldı
# Çünkü 0 değeri mantıksal işlemde False olarak ele alınır
print(True and a or b)
# print(a if True else b)
```

Bu nedenle Python 2.5'ten sonra yukarıdaki riski önlemek için üçlü koşul operatörü eklendi (yukarıdaki kodda yorum satırı yapılan son cümle). O zaman şu soru yeniden ortaya çıkıyor: Yukarıdaki kod daha da kısa yazılabilir mi? Cevap evet.

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', (a if a > b else b) if (a if a > b else b) > c else c)
```

Ama bunu yapmak gerçekten iyi midir? Bu kadar karmaşık bir ifade kodu çok daha anlaşılmaz hale getirmedi mi? Fark ettik ki gerçek geliştirmede pek çok geliştirici bir dilin belirli özelliklerini veya söz dizimi şekerini aşırı kullanmayı seviyor; böylece basit çok satırlı kod, karmaşık tek satırlık ifadeye dönüşüyor. Bunu yapmak gerçekten iyi midir? Bu soruyu ben de kendime defalarca sordum; şu anda verebileceğim cevap, yardımcı fonksiyon kullanan aşağıdaki koddur.

```Python
def the_max(x, y):
	return x if x > y else y


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', the_max(the_max(a, b), c))
```

Yukarıdaki kodda, parametre olarak geçilen iki değerden büyük olanı bulmak için `the_max` adlı yardımcı bir fonksiyon tanımladım; böylece aşağıdaki çıktı ifadesi, üç sayıdan en büyüğünü bulmak için `the_max` fonksiyonunu iki kez çağırabilir; şimdi kodun okunabilirliği çok daha iyi değil mi? Karmaşık ifadeyi yardımcı fonksiyonla değiştirmek gerçekten iyi bir seçimdir; en önemlisi, büyüklük karşılaştırma mantığı bu yardımcı fonksiyona taşındıktan sonra onu yalnızca defalarca çağırmakla kalmaz, kademeli işlem de yapabilirsiniz.

Elbette birçok dilde büyüklük karşılaştırma fonksiyonunu kendiniz gerçekleştirmenize gerek yoktur (genellikle yerleşik fonksiyondur); Python da öyledir. Python'un yerleşik `max` fonksiyonu, Python'un değişken sayıda parametre desteğinden yararlanarak bir seferde birden çok değer veya bir yineleyici geçilip en büyük değeri bulmaya olanak tanır; bu nedenle yukarıda tartıştığımız sorun Python'da tek bir cümledir; ancak karmaşık ifadeden, karmaşık ifadeyi basitleştirmek için yardımcı fonksiyon kullanmaya geçme düşüncesi üzerinde düşünmeye fazlasıyla değer; bu yüzden paylaşıp sizlerle fikir alışverişi yapıyorum.

```Python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('The max is:', max(a, b, c))
```
