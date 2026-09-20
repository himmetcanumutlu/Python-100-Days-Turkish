## Eş Yordamı (Coroutine) Tamamen Anlamanızı Sağlayacak Küçük Bir Örnek

> **Translated to Turkish by** himmetcanumutlu

Eş yordam, Python'da yeni başlayanları en çok zorlayan bilgi noktalarından biridir; aynı zamanda Python'da eş zamanlı programlamayı gerçekleştirmenin önemli bir yoludur. Python'da eş zamanlılık, çok iş parçacığı ve çok süreçle gerçekleştirilebilir; bu iki yol herkesin görece aşina olduğu yöntemlerdir. Aslında eş zamanlılığı gerçekleştirmenin bir yolu daha vardır: asenkron programlama; eş yordam ise asenkron programlamayı gerçekleştirmenin zorunlu yoludur.

Eş yordam, kısaca birbiriyle iş birliği yapan birden çok alt program olarak anlaşılabilir. Aynı iş parçacığı içinde, bir alt program bloklandığında programı hemen o alt programdan diğerine geçirebiliriz; böylece CPU'nun program bloklandığı için boş kalması önlenir ve CPU kullanımı artırılır; yani iş birliğine dayalı bir yöntemle programın yürütülmesi hızlandırılır. Bu nedenle kısaca şunu söyleyebiliriz: **eş yordam, iş birlikçi eş zamanlılığı gerçekleştirir**.

Şimdi küçük bir örnekle iş birlikçi eş zamanlılığın ne olduğunu anlamanıza yardımcı olalım; önce aşağıdaki koda bakın.

```Python
import time


def display(num):
    time.sleep(1)
    print(num)


for num in range(10):
    display(num)
```

Yukarıdaki kodu herkesin kolayca anlayacağına inanıyorum; program 0'dan 9'a kadar sayıları çıktılar; her 1 saniyede bir sayı çıktılanır, bu nedenle tüm programın yürütülmesi yaklaşık 10 saniye sürer. Dikkat edilmesi gereken nokta, çok iş parçacığı veya çok süreç kullanılmadığı için programda yalnızca bir yürütme birimi vardır; `time.sleep(1)` bekletme işlemi ise tüm iş parçacığını 1 saniye durdurur; yukarıdaki kod için bu süre boyunca CPU tamamen boştur ve hiçbir şey yapmaz.

Şimdi eş yordam kullanıldığında ne olduğuna bakalım. Python 3.5'ten itibaren eş yordamla iş birlikçi eş zamanlılığı gerçekleştirmenin daha kullanışlı bir söz dizimi var; `async` ile asenkron fonksiyon tanımlayabiliriz, `await` ile bloklanan bir alt programın CPU'yu kendisiyle iş birliği yapan alt programa devretmesini sağlayabiliriz. Python 3.7'de `async` ve `await` resmî anahtar sözcük hâline geldi ve geliştiricilere büyük sevinç yaşattı. Önce bir asenkron fonksiyonun nasıl tanımlanacağına bakalım.

```Python
import asyncio


async def display(num):
    await asyncio.sleep(1)
    print(num)
```

Şimdi önemli noktaya gelelim. Asenkron fonksiyon, normal fonksiyondan farklıdır; normal fonksiyonu çağırmak dönüş değeri verirken, asenkron fonksiyonu çağırmak bir eş yordam nesnesi verir. Diğer eş yordam nesneleriyle iş birliği etkisini elde etmek için eş yordam nesnesini bir olay döngüsüne koymamız gerekir; çünkü olay döngüsü alt program değiştirme işlemini yönetir; kısacası bloklanan alt programın CPU'yu çalıştırılabilir alt programa devretmesini sağlar.

Önce aşağıdaki liste üreteciyle 10 eş yordam nesnesi oluşturalım; mantığı az önce döngüde `display` fonksiyonunu çağırmakla aynıdır.

```Python
coroutines = [display(num) for num in range(10)]
```

Aşağıdaki kodla olay döngüsü elde edilebilir ve eş yordam nesneleri olay döngüsüne konulabilir.

```Python
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()
```

Yukarıdaki kodu çalıştırdığınızda, her biri 1 saniye bloklanacak 10 eş yordamın toplamda yalnızca yaklaşık 1 saniye bloklandığını görürsünüz; bu da **eş yordam nesnesinin bloklandığında CPU'yu boş bırakmak yerine devrettiğini**, böylece **CPU kullanımını büyük ölçüde artırdığını** gösterir. Ayrıca 0'dan 9'a sayıların, eş yordam nesnelerini oluşturduğumuz sırayla değil de karışık biçimde çıktılandığını fark ederiz; zaten istediğimiz sonuç da budur; ayrıca programı birkaç kez çalıştırırsanız her seferindeki çıktı sırasının farklı olduğunu görürsünüz; bu da eş zamanlı programın yürütme sırasındaki belirsizliğinin sonucudur.

Yukarıdaki örnek, ünlü "Çiçek Kitabı"ndan (《Python İleri Eş Zamanlı Programlama》) gelir; eş yordamı daha derinlemesine kavramanız için orijinal kitaptaki kodda küçük değişiklikler yapılmıştır; örnek basit olsa da iş birlikçi eş zamanlılığın cazibesini size şimdiden hissettirmiştir. Ticari projelerde iş birlikçi eş zamanlılık kullanmanız gerekirse, sistemin varsayılan olay döngüsünü `uvloop`'un sağladığı olay döngüsüyle de değiştirebilirsiniz; böylece daha iyi performans elde edilir; çünkü `uvloop`, ünlü platformlar arası asenkron I/O kütüphanesi libuv temel alınarak gerçekleştirilmiştir. Ayrıca HTTP tabanlı ağ programlama yapacaksanız, üçüncü taraf **aiohttp** kütüphanesi iyi bir seçimdir; asyncio'ya dayanarak asenkron HTTP sunucusu ve istemcisi gerçekleştirir.
