## Python Programlama İdiomları

> **Translated to Turkish by** himmetcanumutlu

"İdiom" sözcüğü "alışılmış yapılış biçimi, olağan yöntem, değişmeyen uygulama" anlamına gelir; bu sözcüğün karşılık geldiği İngilizce kelime "idiom"dur. Python'un diğer birçok programlama dilinden söz dizimi ve kullanım açısından belirgin farkları olduğundan, bir Python geliştiricisi olarak bu idiomlara hâkim olmazsanız "Pythonic" kod yazamazsınız. Aşağıda Python geliştirmede yaygın kullanılan bazı kodları özetledik.

1. Kodun hem içe aktarılabilir hem çalıştırılabilir olmasını sağlayın.

   ```Python
   if __name__ == '__main__':
   ```


2. Mantıksal "doğru" veya "yanlış"ı aşağıdaki biçimde değerlendirin.

   ```Python
   if x:
   if not x:
   ```

   **İyi** kod:

   ```Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': '骆昊', '1002': '王大锤'}
   if name and fruits and owners:
       print('I love fruits!')
   ```

   **Kötü** kod:

   ```Python
   name = 'jackfrued'
   fruits = ['apple', 'orange', 'grape']
   owners = {'1001': '骆昊', '1002': '王大锤'}
   if name != '' and len(fruits) > 0 and owners != {}:
       print('I love fruits!')
   ```

3. `in` operatörünü iyi kullanın.

   ```Python
   if x in items: # içerir
   for x in items: # yineleme
   ```

   **İyi** kod:

   ```Python
   name = 'Hao LUO'
   if 'L' in name:
       print('The name has an L in it.')
   ```

   **Kötü** kod:

   ```Python
   name = 'Hao LUO'
   if name.find('L') != -1:
       print('This name has an L in it!')
   ```

4. Geçici değişken kullanmadan iki değeri takas edin.

   ```Python
   a, b = b, a
   ```

5. String oluşturmak için dizi kullanın.

   **İyi** kod:

   ```Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
   name = ''.join(chars)
   print(name)  # jackfrued
   ```

   **Kötü** kod:

   ```Python
   chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
   name = ''
   for char in chars:
       name += char
   print(name)  # jackfrued
   ```

6. EAFP, LBYL'den üstündür.

   EAFP - **E**asier to **A**sk **F**orgiveness than **P**ermission.

   LBYL - **L**ook **B**efore **Y**ou **L**eap.

   **İyi** kod:

   ```Python
   d = {'x': '5'}
   try:
       value = int(d['x'])
       print(value)
   except (KeyError, TypeError, ValueError):
       value = None
   ```

   **Kötü** kod:

   ```Python
   d = {'x': '5'}
   if 'x' in d and isinstance(d['x'], str) \
   		and d['x'].isdigit():
       value = int(d['x'])
       print(value)
   else:
       value = None
   ```

7. Yineleme için `enumerate` kullanın.

   **İyi** kod:

   ```Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   for index, fruit in enumerate(fruits):
   	print(index, ':', fruit)
   ```

   **Kötü** kod:

   ```Python
   fruits = ['orange', 'grape', 'pitaya', 'blueberry']
   index = 0
   for fruit in fruits:
       print(index, ':', fruit)
       index += 1
   ```

8. Liste oluşturmak için üreteç ifadesi kullanın.

   **İyi** kod:

   ```Python
   data = [7, 20, 3, 15, 11]
   result = [num * 3 for num in data if num > 10]
   print(result)  # [60, 45, 33]
   ```

   **Kötü** kod:

   ```Python
   data = [7, 20, 3, 15, 11]
   result = []
   for i in data:
       if i > 10:
           result.append(i * 3)
   print(result)  # [60, 45, 33]
   ```

9. Sözlük oluşturmak için anahtar ve değerleri `zip` ile birleştirin.

   **İyi** kod:

   ```Python
   keys = ['1001', '1002', '1003']
   values = ['骆昊', '王大锤', '白元芳']
   d = dict(zip(keys, values))
   print(d)
   ```

   **Kötü** kod:

   ```Python
   keys = ['1001', '1002', '1003']
   values = ['骆昊', '王大锤', '白元芳']
   d = {}
   for i, key in enumerate(keys):
       d[key] = values[i]
   print(d)
   ```

> **Açıklama**: Bu yazının içeriği internetten alınmıştır; ilgilenen okuyucular [orijinal yazıyı](http://safehammad.com/downloads/python-idioms-2014-01-16.pdf) okuyabilir.
