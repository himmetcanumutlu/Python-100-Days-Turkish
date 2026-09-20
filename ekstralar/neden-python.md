## Neden Python'u Seçtim

> **Translated to Turkish by** himmetcanumutlu

Günümüzde Python dilinin gelişme ivmesi hem yurt içinde hem yurt dışında durdurulamaz; Python, basit ve zarif söz dizimi ile güçlü ekosistemi sayesinde pek çok dil arasından sıyrılmış ve artık programlama dilleri sıralamasının ilk üçüne sağlam biçimde yerleşmiştir. Yurt içindeki pek çok Python geliştiricisi Java geliştiriciliğinden geçiş yapmıştır; ben de bir istisna değilim. Neden Python'u seçtiğimi kısaca anlatayım.

### Python vs. Java

Aynı işi yaparken Java ve Python kodlarının nasıl yazıldığını birkaç örnekle karşılaştıralım.

Örnek 1: Terminalde "hello, world" çıktılamak.

Java kodu:

```Java
class Test {
	
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
```

Python kodu:

```Python
print('hello, world')
```

Örnek 2: 1'den 100'e kadar toplam.

Java kodu:

```Java
class Test {
    
    public static void main(String[] args) {
        int total = 0;
        for (int i = 1; i <= 100; i += 1) {
            total += i;
        }
        System.out.println(total);
    }
}
```

Python kodu:

```Python
print(sum(range(1, 101)))
```

Örnek 3: Çift renkli top (lotarya) rastgele numara seçimi.

Java kodu:

```Java
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Test {

    /**
     * [min, max) aralığında rastgele tam sayı üret
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    public static void main(String[] args) {
        // Aday kırmızı topları başlat
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        // Altı kırmızı top seç
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        // Kırmızı topları sırala
        Collections.sort(selectedBalls);
        // Bir mavi top ekle
        selectedBalls.add(randomInt(1, 17));
        // Seçilen rastgele numaraları çıktıla
        for (int i = 0; i < selectedBalls.size(); ++i) {
            System.out.printf("%02d ", selectedBalls.get(i));
            if (i == selectedBalls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }
}
```

Python kodu:

```Python
from random import randint, sample

# Aday kırmızı topları başlat
red_balls = [x for x in range(1, 34)]
# Altı kırmızı top seç
selected_balls = sample(red_balls, 6)
# Kırmızı topları sırala
selected_balls.sort()
# Bir mavi top ekle
selected_balls.append(randint(1, 16))
# Seçilen rastgele numaraları çıktıla
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
```

Bu örnekleri gördükten sonra, Python'u seçmemin bir gerekçesi olduğunu kesinlikle hissetmişsinizdir.
