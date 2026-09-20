## PEP 8 Stil Rehberi

> **Translated to Turkish by** himmetcanumutlu

PEP, Python Enhancement Proposal'ın kısaltmasıdır; genellikle "Python Geliştirme Önerisi" olarak çevrilir. Her PEP, Python topluluğuna Python'un daha iyi bir yönde gelişmesine rehberlik eden bir teknik dokümandır; bunlardan 8 numaralı öneri (PEP 8), Python dili için hazırlanmış kod stili rehberidir. Söz diziminde sorun olmaması koşuluyla Python kodunu serbestçe yazabilsek de, gerçek geliştirmede tutarlı bir stille okunabilirliği yüksek kod yazmak her profesyonel programcının yapması gereken bir şeydir ve her şirketin programlama standardında da talep edilir; bu, bir projeyi birden çok kişiyle iş birliği içinde geliştirirken (takım geliştirme) özellikle önemlidir. Bu dokümanı Python resmî sitesindeki [PEP 8 bağlantısından](https://www.python.org/dev/peps/pep-0008/) bulabiliriz; aşağıda bu dokümanın kritik kısımlarının basit bir özetini yapıyoruz.

### Boşluk Kullanımı

1. <u>Girintileme için sekme (Tab) değil, boşluk kullanın.</u> Bu nokta, diğer programlama dillerine alışkın olanlara inanılmaz gelebilir; çünkü programcıların büyük çoğunluğu girintileme için Tab kullanır; ancak bilmelisiniz ki Python'da C/C++ veya Java'daki gibi süslü parantezle kod bloğu oluşturma söz dizimi yoktur; Python'da dallanma ve döngü yapıları, hangi kodların aynı seviyeye ait olduğunu belirtmek için girintileme kullanır; bu nedenle Python kodunun girintilemeye ve girinti genişliğine bağımlılığı diğer birçok dilden çok daha güçlüdür. Farklı editörlerde Tab'in genişliği 2, 4 veya 8 karakter, hatta daha saçma değerler olabilir; Tab ile girintileme yapmak Python kodu için bir felaket olabilir.
2. <u>Söz dizimiyle ilgili her girinti seviyesi 4 boşlukla ifade edilir.</u>
3. <u>Her satırdaki karakter sayısı 79'u geçmemelidir; ifade çok uzun olduğu için birden çok satırı kaplıyorsa, ilk satır dışındaki tüm satırlar normal girinti genişliğine ek olarak 4 boşluk daha eklenmelidir.</u>
4. <u>Fonksiyon ve sınıf tanımlarında, kodun öncesinde ve sonrasında ikişer boş satırla ayrım yapılır.</u>
5. <u>Aynı sınıf içinde, her yöntem arasında bir boş satırla ayrım yapılır.</u>
6. <u>İkili operatörün sol ve sağ tarafında birer boşluk bırakılmalıdır ve yalnızca bir boşluk yeterlidir.</u>

### Tanımlayıcı Adlandırma

PEP 8, Python'daki farklı tanımlayıcıları adlandırmak için farklı adlandırma stillerini benimsemeyi savunur; böylece kodu okurken tanımlayıcının adından, o tanımlayıcının Python'da hangi rolü oynadığı belirlenebilir (bu noktada Python'un kendi yerleşik modülleri ve bazı üçüncü taraf modüller bile çok iyi değildir).

1. <u>Değişken, fonksiyon ve öznitelikler küçük harfle yazılmalıdır; birden çok sözcük varsa alt çizgiyle bağlanmalıdır.</u>
2. <u>Sınıftaki korumalı örnek öznitelikleri tek alt çizgiyle başlamalıdır.</u>
3. <u>Sınıftaki özel örnek öznitelikleri iki alt çizgiyle başlamalıdır.</u>
4. <u>Sınıf ve istisna adlandırmasında her sözcüğün ilk harfi büyük yazılmalıdır.</u>
5. <u>Modül seviyesindeki sabitler tamamen büyük harfle yazılmalıdır; birden çok sözcük varsa alt çizgiyle bağlanmalıdır.</u>
6. <u>Sınıfın örnek yöntemlerinde, nesnenin kendisini göstermek için ilk parametre `self` olarak adlandırılmalıdır.</u>
7. <u>Sınıfın sınıf yöntemlerinde, sınıfın kendisini göstermek için ilk parametre `cls` olarak adlandırılmalıdır.</u>

### İfadeler ve Deyimler

Python'un Zen'inde (`import this` ile görüntülenebilir) şöyle bir ünlü söz vardır: "There should be one-- and preferably only one --obvious way to do it.", Türkçeye çevirisi "Bir işi yapmanın tek ve tercihen yalnızca tek bir açık yolu olmalıdır"; bu cümlenin aktardığı düşünce PEP 8'de de her yerdedir.

1. <u>Olumsuzlamayı satır içi biçimde kullanın, olumsuzlama sözcüğünü tüm ifadenin önüne koymayın.</u> Örneğin `if a is not b`, `if not a is b`'den daha kolay anlaşılır.
2. String, liste vb.nin `None` olup olmadığını veya elemanı olup olmadığını kontrol etmek için uzunluk kontrolü kullanmayın; kontrol için `if not x` gibi bir yazım kullanın.
3. <u>`if` dalı, `for` döngüsü, `except` istisna yakalama vb. içinde yalnızca bir satır kod olsa bile kodu `if`, `for`, `except` vb. ile aynı satıra yazmayın; ayrı yazmak kodu daha net yapar.</u>
4. <u>`import` deyimi her zaman dosyanın başına konur.</u>
5. <u>Modül içe aktarırken `import math` yerine `from math import sqrt` daha iyidir.</u>
6. <u>Birden çok `import` deyimi varsa, bunlar üç bölüme ayrılmalıdır; yukarıdan aşağıya sırasıyla Python **standart modülleri**, **üçüncü taraf modüller** ve **özel modüller**dir; her bölüm içinde modül adının **alfabetik sırasına** göre düzenlenmelidir.</u>
