## Eğlenceli Python

> **Translated to Turkish by** himmetcanumutlu

Aşağıdaki kodların hepsi çok basittir; o kadar basittir ki doğrudan Python'un etkileşimli ortamında tamamlanabilir. Elbette resmî Python'un kendi etkileşimli ortamı görece zor kullanılır; ipython kullanmanızı öneririm; ipython'u aşağıdaki komutla kurabilirsiniz; kurulum başarılı olduktan sonra `ipython` komutunu yazarak etkileşimli ortama girebilirsiniz.

```Shell
pip install ipython
```

veya

```Shell
pip3 install ipython
```

ipython'un en sezgisel avantajları:

1. `?` veya `??` ile yardım alınabilir.
2. `!` ile sistem komutu çağrılabilir.
3. Tab tuşuyla otomatik tamamlama yapılabilir.
4. `%timeit` gibi sihirli yönergeler kullanılabilir.

### Araç Olmadan Kodla Fotoğraf Düzenleme

1. pillow üçüncü taraf kütüphanesini kurun.

   PIL (Python Imaging Library), Python platformunda fiilen standart olan görüntü işleme kütüphanesidir. PIL çok güçlüdür ve API'si çok basit ve kullanışlıdır. Ancak PIL yalnızca Python 2.7'ye kadar destekler ve yıllardır bakım görmemektedir; bu nedenle bir grup gönüllü, PIL temelinde [Pillow](https://github.com/python-pillow/Pillow) adlı uyumlu bir sürüm oluşturdu; Python 3.x'i desteklemenin yanı sıra birçok kullanışlı ve eğlenceli yeni özellik de ekledi.

   ```Shell
   pip install pillow
   ```

   veya

   ```Shell
   pip3 install pillow
   ```

2. Görsel yükleme.

   ```Python
   from PIL import Image
   
   chiling = Image.open('chiling.jpg')
   chiling.show()
   ```

3. Filtre kullanma.

   ```Shell
   from PIL import ImageFilter
   
   chiling.filter(ImageFilter.EMBOSS).show()
   chiling.filter(ImageFilter.CONTOUR).show()
   ```

4. Görseli kırpma ve yapıştırma.

   ```Python
   rect = 220, 690, 265, 740 
   watch = chiling.crop(rect)
   watch.show()
   blured_watch = watch.filter(ImageFilter.GaussianBlur(4))
   chiling.paste(blured_watch, (220, 690))
   chiling.show()
   ```

5. Ayna görüntüsü üretme.

   ```Python
   chiling2 = chiling.transpose(Image.FLIP_LEFT_RIGHT)
   chiling2.show()
   ```

6. Küçük resim (thumbnail) üretme.

   ```Python
   width, height = chiling.size
   width, height = int(width * 0.4), int(height * 0.4)
   chiling.thumbnail((width, height))
   ```

7. Görselleri birleştirme.

   ```Python
   frame = Image.open('frame.jpg')
   frame.show()
   frame.paste(chiling, (210, 150))
   frame.paste(chiling2, (522, 150))
   frame.show()
   ```

Yukarıdaki bilgilerin karşılığı [Python-100-Days](https://github.com/jackfrued/Python-100-Days) projesinin [15. Gün](<https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/15.%E5%9B%BE%E5%83%8F%E5%92%8C%E5%8A%9E%E5%85%AC%E6%96%87%E6%A1%A3%E5%A4%84%E7%90%86.md>) bölümünde de bulunmaktadır.

### WeChat Arkadaşlarına Toplu Tebrik Videosu Gönderme

1. itchat üçüncü taraf kütüphanesini kurun.

   [itchat](<https://itchat.readthedocs.io/zh/latest/>), açık kaynaklı bir WeChat kişisel hesap arayüzüdür; Python ile WeChat'i çağırmak hiç bu kadar kolay olmamıştı.

   ```Shell
   pip install itchat
   ```

   veya

   ```Shell
   pip3 install itchat
   ```

2. WeChat'e giriş yapma.

   ```Python
   import itchat
   
   itchat.auto_login()
   ```

   > Açıklama: Ekranda görünen QR kodu kendi WeChat'inizle taradığınızda giriş işlemi tamamlanır; giriş yaptıktan sonra arkadaş bilgilerinizi alabilir ve arkadaşlarınıza mesaj gönderebilirsiniz.

3. Arkadaşlarınızı bulma.

   ```Python
   friends_list = itchat.get_friends(update=True)
   print(len(friends_list))
   luohao = friends_list[0]
   props = ['NickName', 'Signature', 'Sex']
   for prop in props:
       print(luohao[prop])
   ```

   > Açıklama: friends_list bir listeye eşdeğerdir; listedeki ilk eleman kendinizsiniz.

4. Rastgele 5 arkadaş seçip kullanıcı adlarını, takma adlarını ve imzalarını alma.

   ```Python
   lucky_friends = random.sample(friends_list[1:], 5) 
   props = ['NickName', 'Signature', 'City']
   for friend in lucky_friends:
       for prop in props:
           print(friend[prop] or 'Bu bilgi yok')    
       print('-' * 80)
   ```

5. Arkadaşa metin mesajı gönderme.

   ```Python
   itchat.send_msg('Çöken ruhumu kurtarmak için acil bir kırmızı zarf gerek!!!', toUserName='@8e06606db03f0e28d0ff884083f727e6')
   ```

6. Şanslı arkadaşlara toplu video gönderme.

   ```Python
   lucky_friends = random.sample(friends_list[1:], 5) 
   for friend in lucky_friends:
       username = friend['UserName']
       itchat.send_video('/Users/Hao/Desktop/my_test_video.mp4', toUserName=username)
   ```

itchat ile daha pek çok şey yapılabilir; örneğin bir arkadaşınız size mesaj gönderip geri çektiğinde, bu geri çekilen mesajları görmek isterseniz itchat bunu yapabilir (mesaj alma kancası fonksiyonu kaydedin; [CSDN'deki bir yazıya](<https://blog.csdn.net/enweitech/article/details/79585043>) bakın); yine örneğin, bazen bir arkadaşımızın bizi silip silmediğini veya kara listeye alıp almadığını öğrenmek isteriz; itchat'in sarmaladığı grup sohbeti işleviyle, arkadaş olmayanlar ve kara listedeki kullanıcılar grup sohbetine çekilmez; grup oluşturma fonksiyonunun dönüş değeriyle sizinle belirtilen kişi arasındaki ilişkiyi belirleyebilirsiniz.

### İstemci Kullanmadan Gündemdeki Haberleri Görüntüleme

1. requests kütüphanesini kurun.（[Resmî dokümanı](<https://2.python-requests.org/zh_CN/latest/>) görmek için tıklayın）

   ![](./res/requests.png)

   ```Shell
   pip install requests
   ```

   veya

   ```Shell
   pip3 install requests
   ```

2. Haber verisini kazıma veya API arayüzüyle haber verisi alma.

   ```Python
   import requests
   
   resp = requests.get('http://api.tianapi.com/allnews/?key=lütfen kendi aldığınız Key'i kullanın&col=7&num=50')
   ```

   > Açıklama: Yukarıda Tianxing Data'nın sağladığı veri arayüzü kullanıldı; gerekirse [Tianxing Data](<https://www.tianapi.com/>) sitesinden kendiniz kaydolup etkinleştirebilirsiniz; arayüzü çağırırken kayıt başarılı olduktan sonra sistemin size atadığı key'i doldurmanız gerekir.

3. Ters serileştirmeyle JSON string'ini sözlüğe ayrıştırıp haber listesini alma.

   ```Python
   import json
   
   newslist = json.loads(resp.text)['newslist']
   ```

4. Haber listesinde döngüyle gezinip ilgilendiğiniz haberi bulma, örneğin: Huawei.

   ```Python
   for news in newslist:
       title = news['title']
       url = news['url']
       if 'Huawei' in title:
           print(title)
           print(url)
   ```

5. SMS ağ geçidini çağırıp cep telefonuna SMS gönderme, ilgilenilen haber başlığını bildirip bağlantıyı verme.

   ```Python
   import re
   
   pattern = re.compile(r'https*:\/\/[^\/]*\/(?P<url>.*)') 
   matcher = pattern.match(url)
   
   if matcher:
       url = matcher.group('url')
       resp = requests.post(
           url='http://sms-api.luosimao.com/v1/send.json',
           auth=('api', 'key-lütfen kendi aldığınız Key\'i kullanın'),
           data={
               'mobile': '13548041193',
               'message': f'İlginizi çekebilecek bir haber bulundu - {title}，ayrıntılar için https://news.china.com/{url} adresine tıklayın。【Python Küçük Dersi】'
           },
           timeout=10,
           verify=False
       )
   ```

   > **Açıklama**: Yukarıdaki kod [Luosimao](<https://luosimao.com/>) tarafından sağlanan SMS ağ geçidi hizmetini kullandı; SMS ağ geçidiyle SMS göndermek ücretlidir; ancak genel platformlar birkaç ücretsiz test SMS'i sunar. SMS göndermek platformun kurallarına uymalıdır; kurala aykırı SMS gönderilemez. Yukarıda SMS gönderirken kullanılan SMS şablonu（"İlginizi çekebilecek bir haber bulundu - ###，ayrıntılar için https://news.china.com/### adresine tıklayın。"）ve SMS imzası（"【Python Küçük Dersi】"）Luosimao yönetim platformuna giriş yapılarak yapılandırılmalıdır; nasıl yapılandırılacağını bilmiyorsanız platformun müşteri hizmetleriyle iletişime geçebilirsiniz.
